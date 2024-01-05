"""
URL configuration for Tution_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Learner.views import *
from Tutor.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('courses/',courses,name="courses"),
    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path('otp/',otp,name="otp"),
    path('logout/',logout, name="logout"),
    path('tutor_signup/',tutor_signup,name="tutor_signup"),
    path('tutor_otp/',tutor_otp,name="tutor_otp"),
    path('tutor_login/',tutor_login,name="tutor_login"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
