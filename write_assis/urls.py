from django.contrib import admin
from django.urls import path
from write_assis import views

urlpatterns = [
    path('',views.index,name='index')
]