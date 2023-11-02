from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #comment session
    path('<slug:slug>/', views.details, name='post_details'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    #register login
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    


]
