import json
from django.template import loader
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt


def summary(request):
    template = loader.get_template('project_website/summary.html')
    return HttpResponse(template.render())