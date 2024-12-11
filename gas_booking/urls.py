"""gas_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gas.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('admin_home',admin_home,name='admin_home'),
    path('user_home',user_home,name='user_home'),
    path('logout',logout,name='logout'),
    path('users',users,name='users'),
    path('user_status/<int:id>',user_status,name='user_status'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('complain',complain,name='complain'),
    path('book_gas',book_gas,name='book_gas'),
    path('view_booking',view_booking,name='view_booking'),
    path('delete_booking/<int:id>',delete_booking,name='delete_booking'),
    path('booking_status/<int:id>',booking_status,name='booking_status'),
    path('my_booking',my_booking,name='my_booking'),
    path('view_complains',view_complains,name='view_complains'),
    path('delete_complain/<int:id>',delete_complain,name='delete_complain'),
    path('pay_now/<int:id>',pay_now,name='pay_now'),
    path('invoice/<int:id>',invoice,name='invoice'),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('search',search,name='search'),
    path('search2',search2,name='search2'),
    path('searchday',searchday,name='searchday'),





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
