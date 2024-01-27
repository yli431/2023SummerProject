"""
URL configuration for project_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# from project_website import read_files
from data_import import urls as read_files_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_import/', include("data_import.urls")),
    path('mychatbot/', include("mychatbot.urls")),
    path('report_page/', include("report_page.urls")),
]