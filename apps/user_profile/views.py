from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Profile
from apps.blog.models import Blog
from django.views.generic import DetailView, TemplateView

   
def profile_detail(request, slug):
    
    bookmark_list = Blog.objects.filter(bookmark=request.user)
    print(bookmark_list)
    user = Profile.objects.get(user__username=slug)

    return render(request, "profile/user_profile.html", {'profile': user, 'blogs': bookmark_list})
    
