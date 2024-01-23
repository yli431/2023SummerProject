import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain
from langchain_openai import OpenAI

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
def mychatbot(request):
    api_key = settings.OPENAI_API_KEY
    db_pass = settings.DATABASES["default"]["PASSWORD"]
    
    
    db = SQLDatabase.from_uri(
        f"postgresql+psycopg2://postgres:{db_pass}@localhost:5432/postgres",
    )
    
    # ===========================
    
    db_chain = SQLDatabaseChain.from_llm(
        llm=OpenAI(temperature=0, api_key=api_key, max_tokens=-1, verbose=True), 
        db=db
    )
    
    # question = QUERY.format(question="What is the average value for family income from 2021 to 2023")
    # question = "What is the average value for family income from 2021 to 2023"
    # question = "Do an very detailed analysis for the family income trends from 2000 to 2023"
    question = "What is the 3 year fixed mortgage rate in June 2022?"
    # question = "What is your name?"
    # question = "Will a two-year-old like toys?"
    
    answer = db_chain.invoke(question)
    if answer != 'No, there are no results from the query.':
        llm=OpenAI(temperature=0, api_key=api_key, max_tokens=-1, verbose=True)
        answer = llm.invoke(question)
        return HttpResponse(answer)
    else:    
        return HttpResponse(answer["result"])