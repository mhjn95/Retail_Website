from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('rfqshow',views.rfqshow,name='rfqshow'),
    path('customerlist',views.customerlist,name='customerlist'),
    path('searchforcustomer',views.searchforcustomer,name='searchforcustomer'),
    path('workload',views.workload,name='workload'),
    path('quotesrecieved',views.quotesrecieved,name='quotesrecieved'),
    path('searchformanufacturer',views.searchformanufacturer,name='searchformanufacturer'),
    path('loader/<int:id>',views.searchforsending,name='searchforsending'),
    path('sendinglistmanufacturer<int:id>',views.sendinglistmanufacturer,name='sendinglistmanufacturer'),
    
    ]
