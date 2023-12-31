from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    post = Post.objects.all()
    paginator = Paginator(post,1)

    page_number = request.GET.get("page")
    post_obj = paginator.get_page(page_number)

    
    return render(request, "blog/index.html",{"post": post_obj})

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
    return render(request, 'blog/details.html',{"posts":post, "form":form})
#Comments end here


def blog(request):
    post = Post.objects.all()
    paginator = Paginator(post,2)

    page_number = request.GET.get("page")
    post_obj = paginator.get_page(page_number)

    
    return render(request, "blog/blog.html",{"post": post_obj})


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
            next = request.POST.get('next', '/')
            login(request, user)
            return HttpResponseRedirect(next)
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