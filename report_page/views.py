from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def report_page_template(request):
    template = loader.get_template('report.html')
    return HttpResponse(template.render())
