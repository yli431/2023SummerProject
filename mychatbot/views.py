from django.conf import settings
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from langchain_experimental.sql.base import SQLDatabaseChain

def mychatbot(request: WSGIRequest) -> JsonResponse:
    question = request.GET["ai_question"]
    answer = settings.DB_CHAIN_INSTANCE.invoke(input=question, return_only_outputs=False)
    return JsonResponse({"ai_response": answer["result"]})

def chat_history(request):
    db_chain: SQLDatabaseChain = settings.DB_CHAIN_INSTANCE
    history_chat = db_chain.memory.dict()
    
    contents = history_chat["chat_memory"]["messages"]
    response_list = []
    for content in contents:
        response_list.append(content["content"])
    return JsonResponse({"history": response_list})
