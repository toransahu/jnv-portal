from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    ]