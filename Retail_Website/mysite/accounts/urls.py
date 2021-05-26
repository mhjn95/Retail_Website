from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.login,name='login'),
    path('registercustomer',views.registercustomer,name='registercustomer'),
    path('registerseller',views.registerseller,name='registerseller'),
    path('registermanufacturer',views.registermanufacturer,name='registermanufacturer'),
    path('dashboardadmin',views.dashboardadmin,name='dashboardadmin'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path('orders',views.orders,name='orders'),
    path('history',views.history,name='history'),
    path('quotes',views.quotes,name='quotes'),
    path('accountsettingscustomer',views.accountsettingscustomer,name='accountsettingscustomer'),
    path('accountsettingsmanufacturer',views.accountsettingsmanufacturer,name='accountsettingsmanufacturer'),
    path('currentjob',views.currentjob,name='currentjob'),
    path('write',views.write,name='write'),
    path('blogshow',views.blogshow,name='blogshow'),
    path('showblogmain<int:id>',views.showblogmain,name='showblogmain'),
]
