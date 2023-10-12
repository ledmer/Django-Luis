from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html",{"posts":posts})


def blog(request):
    return render(request, "blog/blog.html")
    
# def blog(request):
#     return render(request, "blog/blog.html")
