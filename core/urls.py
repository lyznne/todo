from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path ('auth/signup/', views.signup_view, name='signup'),
    path ('auth/signin/', views.signin_view, name='signin'),

]
