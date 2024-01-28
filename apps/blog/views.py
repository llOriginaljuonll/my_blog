from django.shortcuts import render
from django.http import HttpResponse

def blog_home(request):
    return HttpResponse('<h1 align="center">Test before doing.</h1>')