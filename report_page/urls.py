from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.report_page_template),
]