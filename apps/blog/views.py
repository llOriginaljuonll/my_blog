from django.shortcuts import render
from .models import Blog

def blog_home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_home.html', {'blogs': blogs})