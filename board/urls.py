from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as django_auth_views

app_name = 'board'

urlpatterns = [
    path('lp/', views.Lp.as_view(), name='lp'),
    path('posts/', views.PostList.as_view(), name = 'post_list'),
    path('', views.Login.as_view(), name = "login"),
    path('logout', django_auth_views.LogoutView.as_view(), name = "logout"),
]