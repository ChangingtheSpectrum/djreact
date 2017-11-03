from django.views import generic
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.views import generic

urlpatterns = [
    url(r'^view2/', views.view2, name='view2'),
    url(r'^$', views.home, name='home'),
]