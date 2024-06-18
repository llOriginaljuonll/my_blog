from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Profile
from apps.blog.models import Blog
from django.views.generic import DetailView, TemplateView



class ProfileDetailView(DetailView):

    model = Profile
    template_name = 'profile/user_profile.html'

    def get_queryset(self):
        pass
        return super().get_queryset()
