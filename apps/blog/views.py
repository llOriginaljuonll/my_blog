from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

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

