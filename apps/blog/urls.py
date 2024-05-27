from django.urls import path
from .views import blog_home, blog_form, blog_detail, blog_edit, blog_delete, blog_like, blog_bookmark_add
urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('blog/write/<int:user_id>', blog_form, name='blog-form'),
    path('blog/edit/<int:blog_id>/', blog_edit, name='blog-edit'),
    path('blog/<int:blog_id>', blog_detail, name='blog-detail'),
    path('blog/delete/<int:blog_id>', blog_delete, name='blog-delete'),
    path('blog/like/<int:pk>', blog_like, name='blog-like'),
    path('blog/bookmark/<int:pk>', blog_bookmark_add, name='blog-bookmark-add')
]
