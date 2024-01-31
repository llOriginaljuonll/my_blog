from django.urls import path
from .views import blog_home, blog_form, blog_detail

urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('blog/write/<int:user_id>', blog_form, name='blog-form'),
    path('blog/<int:blog_id>', blog_detail, name='blog-detail'),
]
