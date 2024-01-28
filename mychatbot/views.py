from django.conf import settings
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest


def mychatbot(request: WSGIRequest) -> JsonResponse:

    question = request.GET["ai_question"]
    answer = settings.DB_CHAIN_INSTANCE.invoke(input=question, return_only_outputs=False)
    return JsonResponse({"ai_response": answer["result"]})




