from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class ContactSeller(models.Model):
    number = PhoneNumberField()
    # zip = models.IntegerField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    category = models.TextField(null=True)
    # is_done = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username


class ContactManufacturer(models.Model):
    number = models.IntegerField(null=True)
    company_name = models.TextField(null=True)
    code = models.IntegerField(null=True)
    status = models.CharField(null=True,max_length=100)
    checkvalue = models.CharField(null=True,max_length=100)
    resources = models.CharField(null=True,max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    category = models.TextField(null=True)

    # is_done = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username


class ContactCustomer(models.Model):
    number = models.IntegerField(null=True)
    ship = models.TextField(blank=True,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    category = models.TextField(null=True)
    # is_done = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username


class AllCustomer(models.Model):
    first_name = models.TextField(default=True,null=True)
    last_name = models.TextField(default=True,null=True)
    number = models.TextField(default=True,null=True)
    email = models.TextField(default=True,null=True)
    username = models.TextField(default=True,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    category = models.TextField(null=True)

    def __str__(self):
        return self.first_name


class AllManufacturer(models.Model):
    first_name = models.TextField(default=True,null=True)
    last_name = models.TextField(default=True,null=True)
    number = models.TextField(default=True,null=True)
    email = models.TextField(default=True,null=True)
    username = models.TextField(default=True,null=True)
    company_name = models.TextField(null=True)
    code = models.IntegerField(null=True)
    status = models.CharField(null=True,max_length=100)
    checkvalue = models.CharField(null=True,max_length=100)
    resources = models.CharField(null=True,max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    category = models.TextField(null=True)

    def __str__(self):
        return self.first_name


class CustomerRfqDetails(models.Model):
    file = models.FileField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    process = models.TextField(blank=True,null=True)
    material = models.TextField(blank=True,null=True)
    adddetails = models.TextField(blank=True,null=True)
    quality = models.IntegerField(blank=True,null=True)
    unique_id = models.IntegerField(blank=True,null=True)
    nearestloc = models.IntegerField(blank=True,null=True)
    leadtime = models.IntegerField(blank=True,null=True)
    pricing = models.IntegerField(blank=True,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.CharField(blank=True,max_length=50,null=True)
    rejecter = models.CharField(blank=True,max_length=50,null=True)


    def __str__(self):
        return self.user_id.username

class QuotesRecieved(models.Model):
    estimatecost = models.CharField(null=True,blank=True,max_length=100)
    estimatedays = models.CharField(null=True,blank=True,max_length=100)
    moreinfo = models.TextField(null=True,blank=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    uname = models.CharField(null=True,blank=True,max_length=100)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    unique_id = models.IntegerField(blank=True,null=True)
    reject = models.CharField(blank=True,max_length=20,null=True)
    fromcustomer = models.CharField(max_length=20,null=True)
    statusquote = models.CharField(blank=True,null=True,max_length=50)
    statuscheck = models.CharField(blank=True,max_length=20,null=True)
    complaint = models.TextField(blank=True,null=True)
    complaintitle = models.TextField(blank=True,null=True)
    complaintmade = models.CharField(blank=True,null=True,max_length=10)
    complaintchoices = models.TextField(blank=True,null=True)
    resolutions = models.TextField(blank=True,null=True)
    resolutionmade = models.CharField(blank=True,null=True,max_length=10)
    # def __str__(self):
    #     return self.user_id

    def __str__(self):
        return self.uname

class Blog(models.Model):
    title = models.CharField(blank=True,null=True,max_length=100)
    content = models.TextField(blank=True,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True,null=True)
    blogid = models.IntegerField(blank=True,null=True)
