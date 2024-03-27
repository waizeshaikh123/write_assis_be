from django.contrib import admin
from django.urls import path
from write_assis import views

urlpatterns = [
    path('',views.index,name='index'),
    path('reviews/',views.reviews,name='reviews'),
    path('about/',views.About,name='About'),
    path('how_to_order/',views.hto,name='hto'),
    path('login/',views.login,name='login'),
    path('sign_up/',views.sign_up,name='signup')
]