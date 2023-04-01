from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def get_question(request, question_id):
    question_text = Question.objects.get(id=question_id)
    reply = f"""Here is question number {question_id}:
    <br>{question_text}"""
    return HttpResponse(reply)
