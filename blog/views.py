from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

posts = [
    {
        'author': 'AnishT',
        'title': 'First Blog Post',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018' 
    },
    {
        'author': 'JohnD',
        'title': 'Second Blog Post',
        'content': 'Second Post Content',
        'date_posted': 'August 30, 2018' 
    }
]

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')

def blogs(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blogs.html', context)

def bloggers(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'blog/bloggers.html', context)