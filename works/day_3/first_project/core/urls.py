from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_msg),
    path('index',views.hello_msg_template),
]