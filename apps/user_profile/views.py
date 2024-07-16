from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Profile
from apps.blog.models import Blog
from .forms import ProfileForm

   
def profile_detail(request, slug):
    
    bookmark_list = Blog.objects.filter(bookmark=request.user)
    user = Profile.objects.get(user__username=slug)

    instance = Profile.objects.get(id=request.user.pk)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('profile:user-profile', user.slug) # Must be separated by a comma.

    return render(request, "profile/user_profile.html", {'profile': user, 'blogs': bookmark_list, 'form': form})

def dashboard(request):

    blogs = Blog.objects.all().order_by("-pk")
    user = Profile.objects.get(user__id=request.user.pk)

    instance = Profile.objects.get(id=request.user.pk)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('profile:user-profile', user.slug)

    return render(request, "dashboard.html", {'blogs': blogs, 'profile': user, 'form': form})
