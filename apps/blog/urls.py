from django.urls import path
from .views import blog_home, blog_form

urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('blog/write/<str:name>', blog_form, name='blog-form'),
]
