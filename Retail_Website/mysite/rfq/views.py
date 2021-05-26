# from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from contacts.models import ContactCustomer,AllCustomer,AllManufacturer,CustomerRfqDetails,QuotesRecieved
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from rfq.models import Rfq
from rfq.choices import resources_choices,status_choices,checkvalue_choices



def rfqshow(request):

    rfqlist = Rfq.objects.filter(is_done=True).order_by('-list_date')
    paginator = Paginator(rfqlist,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    list = AllManufacturer.objects.order_by('-list_date')



    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            list = list.filter(company_name__icontains=keywords)

    if 'code' in request.GET:
        code = request.GET['code']
        if code:
            list = list.filter(code__iexact=code)


    if 'checkvalue' in request.GET:
        checkvalue = request.GET['checkvalue']
        if checkvalue:
            list = list.filter(checkvalue__icontains=checkvalue)


    if 'resources' in request.GET:
        resources = request.GET['resources']
        if resources:
            list = list.filter(resources__icontains=resources)

    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            list = list.filter(status__icontains=status)

    count= Rfq.objects.count()
    context = {
        'rfqdetails' : paged_listings,
        'list':list,
        'count' : count,
        'resources_choices':resources_choices,
        'status_choices':status_choices,
        'checkvalue_choices':checkvalue_choices,
        # 'uid':uid,
    }
    return render(request,'adminpages/rfqshow.html',context)



def customerlist(request):
    list = AllCustomer.objects.order_by('-list_date')
    count = AllCustomer.objects.count()
    paginator = Paginator(list,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'list' : paged_listings,
        'count' : count
    }
    return render(request,'adminpages/customerlist.html',context)



def searchforcustomer(request):
    queryset_list = AllCustomer.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(first_name__icontains=keywords)

    context = {
        'list' : queryset_list,
        'values' : request.GET
    }


    return render(request,'adminpages/searchforcustomer.html',context)




def searchformanufacturer(request):
    queryset_list_man = AllManufacturer.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list_man = queryset_list_man.filter(company_name__icontains=keywords)

    if 'code' in request.GET:
        code = request.GET['code']
        if code:
            queryset_list_man = queryset_list_man.filter(code__iexact=code)


    if 'checkvalue' in request.GET:
        checkvalue = request.GET['checkvalue']
        if checkvalue:
            queryset_list_man = queryset_list_man.filter(checkvalue__icontains=checkvalue)


    if 'resources' in request.GET:
        resources = request.GET['resources']
        if resources:
            queryset_list_man = queryset_list_man.filter(resources__icontains=resources)

    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            queryset_list_man = queryset_list_man.filter(status__icontains=status)


    context = {
        'list' : queryset_list_man,
        'resources_choices':resources_choices,
        'status_choices':status_choices,
        'checkvalue_choices':checkvalue_choices,
        'values' : request.GET,
    }


    return render(request,'adminpages/searchformanufacturer.html',context)




def workload(request):
    list = AllManufacturer.objects.order_by('-list_date')
    count = AllManufacturer.objects.count()
    paginator = Paginator(list,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'list' : paged_listings,
        'resources_choices':resources_choices,
        'status_choices':status_choices,
        'checkvalue_choices':checkvalue_choices,
        'count' : count
    }
    return render(request,'adminpages/workload.html',context)



def quotesrecieved(request):
    data2 = QuotesRecieved.objects.order_by('-list_date')
    paginator = Paginator(data2,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    count = QuotesRecieved.objects.count()
    context = {
        'data':paged_listings,
        'count':count
    }
    return render(request,'adminpages/quotesrecieved.html',context)



def sendinglistmanufacturer(request,id):
    data = AllManufacturer.objects.order_by('-list_date')
    x = id

    # if request.method == 'POST':
    #     if 'send' in request.POST:
    #         company_name = request.POST['company_name']
    #         print(company_name)
    #         print(x)
    #         return redirect(request.path_info)

    if request.method == 'POST':
        if 'send' in request.POST:
            company_name = request.POST['company_name']

            data = Rfq.objects.get(unique_id=x)
            Data = AllManufacturer.objects.get(company_name=company_name)

            Data3 = CustomerRfqDetails.objects.all().filter(user_id=Data.user_id,unique_id=x)
            if Data3:
                messages.error(request,'You have already sent the RFQ to this person !')
                return redirect(request.path_info)
            else:
                Data2 = CustomerRfqDetails(file=data.file,process=data.process,material=data.material,adddetails=data.adddetails,quality=data.quality,unique_id=x,
                                                            nearestloc=data.nearestloc,leadtime=data.leadtime,pricing=data.pricing,user_id=Data.user_id)

                Data2.save()

                messages.success(request,'Your request has been sent !')
                return redirect(request.path_info)


    context = {
        'data':data,
        # 'data2':data2,
        'resources_choices':resources_choices,
        'status_choices':status_choices,
        'x':x,
        'checkvalue_choices':checkvalue_choices,
    }
    return render(request,'adminpages/sendinglistmanufacturer.html',context)



def searchforsending(request,id):
    queryset_list_man = AllManufacturer.objects.order_by('-list_date')
    x = id
    # y = CustomerRfqDetails.objects.get()


    if request.method == 'POST':
        if 'send' in request.POST:
            company_name = request.POST['company_name']

            data = Rfq.objects.get(unique_id=x)
            Data = AllManufacturer.objects.get(company_name=company_name)

            Data3 = CustomerRfqDetails.objects.all().filter(user_id=Data.user_id,unique_id=x)
            if Data3:
                messages.error(request,'You have already sent the RFQ to this person !')
                return redirect(request.path_info)
            else:
                Data2 = CustomerRfqDetails(file=data.file,process=data.process,material=data.material,adddetails=data.adddetails,quality=data.quality,unique_id=x,
                                                            nearestloc=data.nearestloc,leadtime=data.leadtime,pricing=data.pricing,user_id=Data.user_id)

                Data2.save()

                messages.success(request,'Your request has been sent !')
                return redirect(request.path_info)




    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list_man = queryset_list_man.filter(company_name__icontains=keywords)

    if 'code' in request.GET:
        code = request.GET['code']
        if code:
            queryset_list_man = queryset_list_man.filter(code__iexact=code)


    if 'checkvalue' in request.GET:
        checkvalue = request.GET['checkvalue']
        if checkvalue:
            queryset_list_man = queryset_list_man.filter(checkvalue__icontains=checkvalue)


    if 'resources' in request.GET:
        resources = request.GET['resources']
        if resources:
            queryset_list_man = queryset_list_man.filter(resources__icontains=resources)

    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            queryset_list_man = queryset_list_man.filter(status__icontains=status)


    context = {
        'list' : queryset_list_man,
        'x':x,
        'resources_choices':resources_choices,
        'status_choices':status_choices,
        'checkvalue_choices':checkvalue_choices,
        'values' : request.GET,
    }

    return render(request,'adminpages/loader.html',context)
