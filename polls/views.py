from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list,}
    return render(request, "polls/index.html", context)


"""def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = RequestContext(request, {"latest_question_list": latest_question_list,})
    return HttpResponse(template.render(context))"""


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    response = "You're looking at the results of questing %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)