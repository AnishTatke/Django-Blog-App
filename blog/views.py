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
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')