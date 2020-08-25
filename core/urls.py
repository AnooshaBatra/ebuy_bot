from django.urls import path, include
from django.contrib import admin
from core import views
from allauth.account import views as allauth_views
from allauth.account.views import LoginView as lv



urlpatterns = [
    path('log', views.log),
    path('dash', views.dash),
    path('dashboard', views.dashboard, name="dash_log"),
    path("login/", lv.as_view(), name="account_login"),
    path('',allauth_views.LoginView.as_view()),
    path('logout',allauth_views.LogoutView.as_view()),
    path('launch', views.launch)
    
]