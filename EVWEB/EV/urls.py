
from django.urls import path,include
from .views import *
from EV import views
urlpatterns = [
    path("", EVListView.as_view(), name= 'list'),
    path("add/", EVCreateView.as_view(), name='add'),
    path("detail/", EVDetailView.as_view(), name='detail'),
    path('index/', views.index, name='index'),
    path('login/', views.loginProc, name='login'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('ex1/', views.naverMapEx1),
    path('ex2/', views.naverMapEx2),
    path('ex3/', views.naverMapEx3),
]