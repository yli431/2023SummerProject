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
# QUERY = """
# Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
# Use the following format:

# Question: "Question here"
# SQLQuery: "SQL Query to run"
# SQLResult: "SQLQuery result"
# Answer: "Answer here"

# {question}
# """


# Create your views here.

def mychatbot(request: WSGIRequest) -> JsonResponse:
    # api_key = settings.OPENAI_API_KEY
    # db_pass = settings.DATABASES["default"]["PASSWORD"]
    
    # db = SQLDatabase.from_uri(
    #     f"postgresql+psycopg2://postgres:{db_pass}@localhost:5432/postgres",
    # )
    
    # ===========================
    
    # db_chain = SQLDatabaseChain.from_llm(
    #     llm=OpenAI(temperature=0, api_key=api_key, max_tokens=-1, verbose=True), 
    #     db=db,
    #     memory=ConversationBufferMemory(return_messages=True)
    # )
    
    # question = QUERY.format(question="What is the average value for family income from 2021 to 2023")
    # question = "What is the average value for family income from 2021 to 2023"
    # question = "Do an very detailed analysis for the family income trends from 2000 to 2023"
    # question = "What is the 3 year fixed mortgage rate in June 2022?"
    # question = "abc"
    # question = "Will a two-year-old like toys?"
    print("00000000000000000")
    print(request.GET)
    question = request.GET["ai_question"]
    # return JsonResponse({"ai_response": "222"})
    answer = settings.DB_CHAIN_INSTANCE.invoke(input=question, return_only_outputs=False)
    print("11111111111111111")
    print(answer)
    # # return HttpResponse("123")
    return JsonResponse({"ai_answer": answer["result"]})
    
    
def try_template(request):
    template = loader.get_template('test_template.html')
    return HttpResponse(template.render())




