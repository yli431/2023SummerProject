from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('mychatbot/', views.mychatbot),
    path('try_template/', views.try_template),
]

