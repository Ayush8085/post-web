# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # path('login/', auth_views.LoginView.as_view(template_name='loginsys/login.html'), name='login'),

    path('login/', views.loginUser, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register-user/', views.registerUser, name='register-user'),
]
