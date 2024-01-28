import json
from django.template import loader
from django.http import HttpResponse


def summary(request):
    template = loader.get_template('project_website/summary.html')
    return HttpResponse(template.render())