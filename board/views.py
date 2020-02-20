from django.shortcuts import render
from django.views import generic

# Create your views here.
class Lp(generic.TemplateView):
    template_name = 'board/lp.html'