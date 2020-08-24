from django.urls import path, include
from django.contrib import admin
from core import views
from allauth.account import views as allauth_views



urlpatterns = [
    path('dashboard', views.dashboard),
    
    path('log', views.log),
    path('',allauth_views.LoginView.as_view()),
    path('logout',allauth_views.LogoutView.as_view()),
    path('launch', views.launch)
    
]