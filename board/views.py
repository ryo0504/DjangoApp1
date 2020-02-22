from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
class Lp(generic.TemplateView):
    template_name = 'board/lp.html'

class PostList(generic.TemplateView):
    template_name = 'board/post_list.html'