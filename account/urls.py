from django.urls import  path
from account import views

urlpatterns = [
    path('', views.list_all, name='list_all'),
    path('create/', views.create, name='create'),
    ]