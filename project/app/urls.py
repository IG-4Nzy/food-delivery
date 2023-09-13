from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    path("",views.log_sin,name="log_sin"),
    path("login",views.login,name="login" ),
    path("sigup",views.signup,name="signup" ),


]