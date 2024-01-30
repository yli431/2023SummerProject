from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def dashboard_views(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())