from django.conf import settings
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from langchain_experimental.sql.base import SQLDatabaseChain
import openai
import sqlalchemy.exc


def mychatbot(request: WSGIRequest) -> JsonResponse:
    question = request.GET["ai_question"]    
    try:
        answer = settings.DB_CHAIN_INSTANCE.invoke(input={"query": question}, return_only_outputs=True)
    except sqlalchemy.exc.ProgrammingError as error:
        print(error)
        return JsonResponse({"ai_response": "[ERROR] The question can not be parsed by the system, please reorganize the question..."})
    except openai.BadRequestError as error:
        print(error)
        return JsonResponse({"ai_response": "[ERROR] The answer of the question may be over limitation, please ask another one..."})

    return JsonResponse({"ai_response": answer["result"]})


def chat_history(request: WSGIRequest) -> JsonResponse:
    db_chain: SQLDatabaseChain = settings.DB_CHAIN_INSTANCE
    history_chat = db_chain.memory.dict()  # type: ignore
    
    contents = history_chat["chat_memory"]["messages"]
    response_list = []
    for content in contents:
        response_list.append(content["content"])
    return JsonResponse({"history": response_list})
