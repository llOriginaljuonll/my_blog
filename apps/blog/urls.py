from django.urls import path
from .views import blog_home, blog_form, blog_detail, blog_edit

urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('blog/write/<int:user_id>', blog_form, name='blog-form'),
    path('blog/edit/<int:blog_id>/', blog_edit, name='blog-edit'),
    path('blog/<int:blog_id>', blog_detail, name='blog-detail'),
]
