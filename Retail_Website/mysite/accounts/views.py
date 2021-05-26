from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from contacts.models import ContactSeller,ContactManufacturer,ContactCustomer,AllCustomer,AllManufacturer,CustomerRfqDetails,QuotesRecieved,Blog
from rfq.models import Rfq
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
import schedule
import time

def registercustomer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        number = request.POST.get('number2')
        category = 'Customer'


        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('registercustomer')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('registercustomer')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.is_staff=False;
                    user.is_superuser=False;
                    user.save()


                    allcustomer = AllCustomer(username=username,email=email,first_name=first_name,last_name=last_name,category='Customer')
                    allcustomer.user_id = user
                    allcustomer.save()


                    send_mail(
                    'Machine WorkX',
                    'Thank you '+ first_name + ' for showing interest in our website. Login in with us and enjoy marketing.You have registered as a CUSTOMER',
                    'aayushmahajan950@gmail.com',
                    [email],
                    fail_silently = False
                    )

                    u_id = User.objects.get(username=username)
                    addusr = ContactCustomer(user_id=u_id,number=number,category='Customer')

                    u_id2 = AllCustomer.objects.get(username=username)
                    u_id2.number=number
                    u_id2.save()

                    addusr.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')


        else:
            messages.error(request,'Passwords do not match')
            return redirect('registercustomer')
    else:
        return render(request,'accounts/registercustomer.html')



def registerseller(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        number = request.POST['number']
        category = 'Seller'
        # zip = request.POST['zip']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('registerseller')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('registerseller')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    # all = All(username=username,email=email,first_name=first_name,last_name=last_name,category = 'Seller')
                    # all.save()
                    user.is_staff=True;
                    user.is_superuser=False;
                    user.save()

                    send_mail(
                    'Machine WorkX',
                    'Thank you '+ first_name + ' for showing interest in our website. Login in with us and enjoy marketing.You have registered as a SELLER',
                    'aayushmahajan950@gmail.com',
                    [email],
                    fail_silently = False
                    )

                    u_id = User.objects.get(username=username)
                    #reference ,primary key line 74
                    addusr = ContactSeller(user_id=u_id,number=number,category = 'Seller')

                    # u_id2 = All.objects.get(username=username)
                    # u_id2.number=number
                    # u_id2.save()

                    addusr.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request,'Passwords do not match')
            return redirect('registerseller')
    else:
        return render(request,'accounts/registerseller.html')



def registermanufacturer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        number = request.POST.get('number1')
        code = request.POST.get('code')
        company_name = request.POST.get('company_name')
        category = 'Manufacturer'


        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('registermanufacturer')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('registermanufacturer')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.is_staff=False;
                    user.is_superuser=True;
                    user.save()

                    allmanufacturer = AllManufacturer(username=username,email=email,first_name=first_name,last_name=last_name,category = 'Manufacturer')
                    allmanufacturer.user_id = user
                    allmanufacturer.save()



                    send_mail(
                    'Machine WorkX',
                    'Thank you '+ first_name + ' for showing interest in our website. Login in with us and enjoy marketing.You have registered as a MANUFACTURER',
                    'aayushmahajan950@gmail.com',
                    [email],
                    fail_silently = False
                    )

                    u_id = User.objects.get(username=username)
                    addusr = ContactManufacturer(user_id=u_id,code=code,company_name=company_name,number=number,category = 'Manufacturer')

                    u_id2 = AllManufacturer.objects.get(username=username)
                    u_id2.number=number
                    u_id2.company_name=company_name
                    u_id2.code = code

                    u_id2.save()

                    addusr.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request,'Passwords do not match')
            return redirect('registermanufacturer')
    else:
        return render(request,'accounts/registermanufacturer.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')

            # auth.login(request,user)
            # if request.user.is_staff and request.user.is_superuser:
                # print('Welcome admin')
                # return redirect('dashboardadmin')   tick
            # messages.success(request,"Logged In")
            # else:             tick


        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def dashboardadmin(request):
    return render(request,'accounts/dashboardadmin.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request,"You are now logged out")
        return redirect('index')


def dashboard(request):
    # MANUFACTURER
    if not request.user.is_staff and request.user.is_superuser:
        user=request.user
        data=ContactManufacturer.objects.get(user_id=user)
        DataAll = AllManufacturer.objects.get(user_id=user)
        Data2 = CustomerRfqDetails.objects.filter(user_id=user).order_by('-unique_id')

        if request.method == 'POST':
            if 'status' in request.POST:
                status = request.POST['status']
                DataAll = AllManufacturer.objects.get(user_id=user)
                Data = ContactManufacturer.objects.get(user_id=user)
                DataAll.status = status
                Data.status = status
                DataAll.save()
                Data.save()
                return redirect(request.path_info)

            if 'submitoffer' in request.POST:
                estimatedays = request.POST['estimatedays']
                estimatecost = request.POST['estimatecost']
                moreinfo = request.POST['moreinfo']
                unique_id = request.POST['unique_id']
                # user = request.user
                data = AllManufacturer.objects.get(user_id=user)
                Data2 = Rfq.objects.get(unique_id=unique_id)
                Data3 = QuotesRecieved.objects.all().filter(user_id=data.user_id,unique_id=unique_id)
                if Data3:
                    messages.error(request,'You have already responded for this RFQ  !')
                    return redirect(request.path_info)
                else:
                    Data = QuotesRecieved(estimatecost=estimatecost,statusquote='Not Accepted Yet by Customer',reject='False',estimatedays=estimatedays,moreinfo=moreinfo,user_id=data.user_id,uname=data.username,unique_id=Data2.unique_id,fromcustomer=Data2.user_id)
                    Data.save()
                    messages.success(request,'Your response has been recorded !')
                    return redirect(request.path_info)

            if 'reject' in request.POST:
                unique_id = request.POST['unique_id']
                data = AllManufacturer.objects.get(user_id=user)
                Data2 = Rfq.objects.get(unique_id=unique_id)

                Data3 = QuotesRecieved.objects.all().filter(user_id=data.user_id,unique_id=unique_id)
                if Data3:
                    messages.error(request,'You have already responded for this RFQ  !')
                    return redirect(request.path_info)
                else:
                    Data = QuotesRecieved(user_id=data.user_id,uname=data.username,unique_id=Data2.unique_id,fromcustomer=Data2.user_id)
                    Data.save()
                    Data3 = CustomerRfqDetails.objects.get(user_id=data.user_id,unique_id=Data2.unique_id)
                    Data3.rejecter = "yes"
                    Data3.save()

                    messages.success(request,'The RFQ has been rejected !')
                    return redirect(request.path_info)

        context={
            'data':data,
            'DataAll':DataAll,
            'list':Data2,
        }
        return render(request,'accounts/dashboardmanufacturer.html',context)




        # seller
    elif request.user.is_staff and not request.user.is_superuser:
        user=request.user
        data=ContactSeller.objects.get(user_id=user);
        context={
            'data':data
        }
        return render(request,'accounts/dashboardseller.html',context)



    elif not request.user.is_staff and not request.user.is_superuser:
        user=request.user
        if request.method == 'POST':
            file = request.FILES['file']
            process = request.POST['process']
            material = request.POST['material']
            adddetails = request.POST['adddetails']
            quality = request.POST['quality']
            nearestloc = request.POST['nearestloc']
            leadtime = request.POST['leadtime']
            pricing = request.POST['pricing']
            user = request.user
            count= Rfq.objects.count()
            unique_id = count+1;
            Data = Rfq(user_id=user,file=file,
            process = process,
            material = material,
            adddetails = adddetails,
            quality = quality,
            nearestloc = nearestloc,
            leadtime = leadtime,
            pricing = pricing,unique_id=unique_id)
            messages.success(request,"request made")
            Data.save()
            return redirect(request.path_info)

        data=ContactCustomer.objects.get(user_id=user)

        context={
            'data':data,

        }

        return render(request,'accounts/dashboardcustomer.html',context)

# admin
    elif request.user.is_staff and request.user.is_superuser:
        user = request.user
        data = QuotesRecieved.objects.all().filter(complaintmade='Yes')
        paginator = Paginator(data,10)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        count = QuotesRecieved.objects.filter(complaintmade='Yes').count()
        context = {
            'data':paged_listings,
            'count':count
        }
        return render(request,'accounts/dashboardadmin.html',context)

# def changepass(request):
#     return render(request,'accounts/changepass.html')




def quotes(request):
    user=request.user
    list = QuotesRecieved.objects.all().filter(fromcustomer=user,reject='False')
    count = QuotesRecieved.objects.all().filter(fromcustomer=user,reject='False').count()
    # Data = AllManufacturer.objects.get(username=list.user_id)
    paginator = Paginator(list,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    if request.method == 'POST':
        if 'accept' in request.POST:
            unique_id = request.POST['unique_id']
            uname = request.POST['uname']

            x = AllManufacturer.objects.get(username=uname)
            Data = QuotesRecieved.objects.all().filter(unique_id=unique_id,statusquote='Accepted by Customer')
            Data4 = CustomerRfqDetails.objects.get(unique_id=unique_id,user_id=x.user_id)

            if Data:
                messages.error(request,'You have already responded to the RFQ with this ID !')
                return redirect(request.path_info)
            else:
                data = QuotesRecieved.objects.get(unique_id=unique_id,uname=uname)
                data.statusquote = 'Accepted by Customer'
                data.statuscheck = 'Done'
                data.complaintmade = 'No'
                data.resolutionmade = 'No'
                data.resolutions = 'No resolution has been given yet'
                data.save()
                Data4.status = 'This has been Accepted by customer !'
                # user=request.user
                Data4.save()
                messages.success(request,'You have accepted this quote')
                return redirect(request.path_info)

    context = {
        'list':paged_listings,
        'count':count,
        # 'data':Data,
    }
    return render(request,'accounts/quotes.html',context)

def orders(request):
    return render(request,'accounts/orders.html')

def history(request):
    user = request.user
    data = QuotesRecieved.objects.filter(fromcustomer=user,statusquote='Accepted by Customer').order_by('-list_date')
    count = QuotesRecieved.objects.filter(fromcustomer=user,statusquote='Accepted by Customer').order_by('-list_date').count()
    paginator = Paginator(data,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    if request.method == "POST":
        if 'complaint' in request.POST:
            unique_id = request.POST['unique_id']
            complain = request.POST['complain']
            complaintitl = request.POST['complaintitle']
            uname = request.POST['uname']
            options = request.POST['complaintoptions']
            print(unique_id)
            Data = QuotesRecieved.objects.all().filter(unique_id=unique_id,fromcustomer=user,uname=uname,statusquote='Accepted by Customer',complaintmade='No')
            if Data:
                Data2 = QuotesRecieved.objects.get(fromcustomer=user,unique_id=unique_id,uname=uname)
                Data2.complaint = complain
                Data2.complaintitle = complaintitl
                Data2.complaintmade = 'Yes'
                Data2.complaintchoices = options
                Data2.save()
                messages.success(request,'You have successfully made the complaint')
                return redirect(request.path_info)

            else:
                messages.error(request,'You have already made a complaint !')
                return redirect(request.path_info)


    context = {
        'data':paged_listings,
        'count':count
    }
    return render(request,'accounts/history.html',context)

def accountsettingscustomer(request):
    user=request.user
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        ship = request.POST['ship']
        # username = request.POST['username']
        # email = request.POST['email']
        user=request.user

        Data = ContactCustomer.objects.get(user_id=user)
        DataAll = AllCustomer.objects.get(user_id=user)
        data=User.objects.get(username=user);

        data.first_name=first_name
        data.last_name=last_name
        DataAll.first_name = first_name
        DataAll.last_name = last_name
        Data.ship = ship

        DataAll.save()
        Data.save()
        # data.email=email
        data.save()

        return redirect(request.path_info)


    data=ContactCustomer.objects.get(user_id=user)
    context={
        'data':data
        }
    return render(request,'accounts/accountsettingscustomer.html',context)


def currentjob(request):
    user = request.user
    data = QuotesRecieved.objects.all().filter(uname=user,complaintmade='Yes').order_by('-list_date')
    count = QuotesRecieved.objects.all().filter(uname=user,complaintmade='Yes').count()
    paginator = Paginator(data,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    if request.method == 'POST':
        if 'resol' in request.POST:
            resolution = request.POST['resolutiontext']
            unique_id = request.POST['unique_id']
            # fm = request.POST['fromcustomer']
            print(unique_id)
            # print(fm)

            Data = QuotesRecieved.objects.all().filter(unique_id=unique_id,user_id=user,statusquote='Accepted by Customer',resolutionmade='No')
            if Data:
                Data2 = QuotesRecieved.objects.get(unique_id=unique_id,user_id=user)
                Data2.resolutions = resolution
                Data2.resolutionmade = 'Yes'
                Data2.save()
                messages.success(request,"You have successfully sent the resolution")
                return redirect(request.path_info)

            else:
                messages.error(request,"Already responded")
                return redirect(request.path_info)





    context = {
        'data':paged_listings,
        'count':count,
    }
    return render(request,'accounts/currentjob.html',context)


def accountsettingsmanufacturer(request):
    user=request.user
    if request.method == 'POST':

        if 'checkvalue' in request.POST:
            checkvalue = request.POST['checkvalue']
            DataAll = AllManufacturer.objects.get(user_id=user)
            Data = ContactManufacturer.objects.get(user_id=user)
            DataAll.checkvalue = checkvalue
            Data.checkvalue = checkvalue
            DataAll.save()
            Data.save()

            return redirect(request.path_info)


        if 'resources' in request.POST:
            resources = request.POST['resources']
            DataAll = AllManufacturer.objects.get(user_id=user)
            Data = ContactManufacturer.objects.get(user_id=user)
            DataAll.resources = resources
            Data.resources = resources
            DataAll.save()
            Data.save()

            return redirect(request.path_info)

        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            number = request.POST['number']
            user=request.user

            Data = ContactManufacturer.objects.get(user_id=user)
            DataAll = AllManufacturer.objects.get(user_id=user)
            data=User.objects.get(username=user)

            data.first_name=first_name
            data.last_name=last_name
            # data.number = number
            DataAll.first_name = first_name
            DataAll.last_name = last_name
            DataAll.number = number
            Data.number = number

            DataAll.save()
            data.save()
            Data.save()
            return redirect(request.path_info)





    data=ContactManufacturer.objects.get(user_id=user)
    context={
        'data':data
        }
    return render(request,'accounts/accountsettingsmanufacturer.html',context)


def write(request):
    if request.method=="POST":
        if 'postb' in request.POST:
            cont = request.POST['cont']
            title = request.POST['title']
            file = request.FILES.get('file')
            count= Blog.objects.count()
            idnumber = count+1;
            data = Blog(content=cont,title=title,photo_main=file,blogid=idnumber)
            data.save()
            messages.success(request,'You just made a blog !')
            return redirect(request.path_info)

        if 'postbedit' in request.POST:
            cont2 = request.POST['contedit']
            title2 = request.POST['titleedit']
            file2 = request.FILES.get('fileedit')
            idnumber = request.POST['b_id']
            DataAll = Blog.objects.get(blogid=idnumber)
            DataAll.title = title2
            DataAll.content = cont2
            DataAll.photo_main = file2
            DataAll.save()
            messages.success(request,'Post has been modified !')
            return redirect(request.path_info)


    # Data = Blog.objects.all()
    x = Blog.objects.order_by('-list_date')
    count = Blog.objects.count()
    paginator = Paginator(x,5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'data':paged_listings,
    }

    return render(request,'adminpages/write.html',context)

def blogshow(request):
    x = Blog.objects.order_by('-list_date')
    count = Blog.objects.count()
    paginator = Paginator(x,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'x':x,
        'count':count,
        'list':paged_listings

    }
    return render(request,'pages/blogshow.html',context)

def showblogmain(request,id):
    data = Blog.objects.get(blogid=id)
    context = {
        'data':data,
    }
    return render(request,'adminpages/showblogmain.html',context)
