from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html",{"posts":posts})


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
            next_url = request.POST.get('next', None)
            if next_url:
                return redirect(next_url)
            else:
            # If 'next' is not present, use the stored URL or a default URL
                return redirect(request.session.get('last_page_visited', '/'))
        else:
            messages.info(request, 'Username OR Password is incorrect')
    else:
        request.session['last_page_visited'] = request.META.get('HTTP_REFERER', '/')
 
    context = {}
    return render(request, "accounts/login.html", context)

def logoutUser(request):
    request.session['last_page_visited'] = request.META.get('HTTP_REFERER', '/')
    next_url = request.GET.get('next', None)

    logout(request)
    return redirect(next_url or request.session.get('last_page_visited', '/'))
def signupPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,'Account was created for ' + user)
            return redirect('/')
            
    context = {'form':form}
    return render(request, "accounts/signup.html",context)