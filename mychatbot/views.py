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


def mychatbot(request: WSGIRequest) -> JsonResponse:

    question = request.GET["ai_question"]
    answer = settings.DB_CHAIN_INSTANCE.invoke(input=question, return_only_outputs=False)
    print("1111111111111111")
    print(question)
    return JsonResponse({"ai_response": answer["result"]})
    
    
def try_template(request):
    template = loader.get_template('test_template.html')
    return HttpResponse(template.render())




