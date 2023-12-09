from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from django.core.paginator import Paginator
# Create your views here.

def index(request):
    post = Post.objects.all()
    
    return render(request, "blog/index.html",{"post": post})

#Comments
def details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', slug=slug)

    else:
        form = CommentForm()
    return render(request, 'blog/details.html',{"post":post, "form":form})
#Comments end here


def blog(request):
    return render(request, "blog/blog.html")

def about(request):
    return render(request, "blog/about.html")
# def blog(request):
#     return render(request, "blog/blog.html")


#Accounts
def loginPage(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('next')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, "accounts/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('/')
def signupPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
            
    context = {'form':form}
    return render(request, "accounts/signup.html",context)
