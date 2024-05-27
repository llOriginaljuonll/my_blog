from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from .models import Blog

def blog_home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_home.html', {'blogs': blogs})

def blog_form(request, user_id):
    if request.method == 'POST':
        blog = Blog(writer=request.user)
        form = BlogForm(request.POST, instance=blog)
       
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'blog_form.html', {'form': form, 'user_id': user_id})
    else:
        form = BlogForm()
        return render(request, 'blog_form.html', {'form': form})
    
def blog_detail(request, blog_id):

    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_edit(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = BlogForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'blog_edit.html', {'form': form, 'blog': blog})

def blog_delete(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog has been successfully deleted')
    return redirect('/')

def blog_like(request, pk):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, id=pk)
        if blog.likes.filter(id=request.user.id):
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('blog:blog-home')
    
def blog_bookmark_add(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if blog.bookmark.filter(pk=request.user.id).exists():
        blog.bookmark.remove(request.user)
    else:
        blog.bookmark.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])