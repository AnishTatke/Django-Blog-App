from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('blogs/', views.blogs, name='blogs-list'),
    path('bloggers/', views.bloggers, name='bloggers-list')
]