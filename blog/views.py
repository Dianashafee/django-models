from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog
# Create your views here.


class HomeView(ListView):
    template_name = 'home.html'
    model = Blog

class BlogDetailsView(DetailView):
    template_name = 'post_detail.html'
    model = Blog