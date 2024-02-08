import json
from django.template import loader
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


def summary(request: WSGIRequest) -> HttpResponse:
    template = loader.get_template('project_website/summary.html')
    return HttpResponse(template.render())