from django.urls import path

from bkapp import views, admin


app_name='bkapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('loginsuccess/',views.loginsuccess,name='loginsuccess'),
    path('last/',views.last,name='last'),
    path('form/',views.form,name='form'),
    path('check/',views.check,name='check'),
    path('logout',views.logout,name='logout')
]