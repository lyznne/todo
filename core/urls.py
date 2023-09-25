from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path ('auth/signup/', views.signup_view, name='signup'),
    path ('auth/signin/', views.signin_view, name='signin'),
    path ('auth/signout/', views.signout_view, name='signout'),
    path('home/', views.home_view, name='home'), 
    path('home/profile', views.profile_view, name='profile'), 
    path('home/create-task/', views.create_task_view, name='create-task'), 
]
