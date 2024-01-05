from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice

def index(request):
    Question.objects.create(
        question_text="liupangpang222",
        pub_date="2024-02-01"
    )
    
    # all_data = read_csv("mydata.csv")
    # for data in all_data:
    #     Question.objects.create(
    #         question_text=data["question_text"],
    #         pub_date=data["pub_date"],
    #     )
    # try:
    #     all_choices = Choice.objects.filter(votes__gte=3).order_by("votes"
    #                                                     )
    # except Exception as e:
    #     print(e)
    # for choice in all_choices:
    #     print("================")
    #     print(choice.choice_text)
    #     print(choice.votes)
    #     print(choice.question.question_text)
    
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    try:
        my_response = HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)
    return my_response


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
