from django.urls import path
from .views import blog_home, blog_form, blog_detail

urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('blog/write/<str:name>', blog_form, name='blog-form'),
    path('blog/<int:blog_id>', blog_detail, name='blog-detail'),
]
