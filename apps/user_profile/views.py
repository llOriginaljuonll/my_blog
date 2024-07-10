from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Profile
from apps.blog.models import Blog
from django.views.generic import DetailView, TemplateView

   
def profile_detail(request, slug):
    
    bookmark_list = Blog.objects.filter(bookmark=request.user)
    user = Profile.objects.get(user__username=slug)

    return render(request, "profile/user_profile.html", {'profile': user, 'blogs': bookmark_list})

def dashboard(request):

    blogs = Blog.objects.all().order_by("-pk")
    user = Profile.objects.get(user__id=request.user.id)

    return render(request, "dashboard.html", {'blogs': blogs, 'profile': user})