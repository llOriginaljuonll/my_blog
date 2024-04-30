from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login

class SignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('blog:blog-home')
    template_name = 'registration/sign_up.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid