"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from signup.views import signaction
from login.views import loginaction
from website.views import request
from website.views import home
from website.views import about
from website.views import submitted
# from website
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('',loginaction),
    path('request/',request),
    path('home/',home),
    path('about/',about),
    path('request/submitted',submitted),
    path('track/',views.track),
    path('track/trackingdetails',views.trackingdetails),
    path('adminlogin/',views.AdminSignin),
    # path('adminsignup/',views.AdminSignup),
    # path('adminsignup/Signup',views.Signup),
    path('adminlogin/Login',views.Login),
    # path('adminsignup/Login',views.Login)
    
]
