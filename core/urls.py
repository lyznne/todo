from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path ('auth/signup/', views.signup_view, name='signup'),
    path ('auth/signin/', views.signin_view, name='signin'),
    path ('auth/signout/', views.signout_view, name='signout'),
    
    path('home/profile', views.profile_view, name='profile'), 
    path ('auth/profile/update-profile', views.update_profile_view, name='update_profile'),
    path ('auth/profile/update-password', views.update_password_view, name='update_password'),
    path ('auth/profile/del:user_id', views.delete_profile_view, name='delete_profile'),
    
    
    path('home/', views.home_view, name='home'), 
    path('home/create-task/', views.create_task_view, name='create-task'), 
    
    path("home/singletask/create", views.single_task_view, name="single_task"),
    path("home/singletask/update", views.update_task_status, name="update_task_status"),
    path("home/singletask/delete", views.delete_single_task, name="del_single_task"),
]
