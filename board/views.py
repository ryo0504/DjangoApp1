from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from django.contrib.auth.views import LoginView 
from .forms import * 
from django.contrib.auth import login
from django.urls import reverse
from .forms import SignUpForm
from .models import User


# Create your views here.
class Lp(generic.TemplateView):
    template_name = 'board/lp.html'


class PostList(generic.TemplateView):
    template_name = 'board/post_list.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'board/login.html'


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'board/sign_up.html' 
    
    def get_success_url(self):
        form = self.get_form()
        # usernameから登録したユーザー情報を参照
        user = User.objects.get(name=form.data.get('name'))

        # ログイン処理を行う
        login(self.request, user)
        return reverse('board:post_list')
    

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'board/user_detail.html'
