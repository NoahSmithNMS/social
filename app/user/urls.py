"""
URL Mappings for the user API.
"""
from django.urls import path, include

from user import views


app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    #path('register/', views.register, name='register'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logoutt'),
    path('current/', views.UserView.as_view(), name='current'),
]
