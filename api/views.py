# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
from django.http import HttpResponseNotFound

# Create your views here.



@api_view(['GET'])
def questions_list(request):
    questions = Question.objects.filter(is_approved=True)
    try:
        questions = questions.filter(topic=request.GET.get('topic')) if request.GET.get('topic') else questions
        questions = questions.filter(grade=request.GET.get('grade')) if request.GET.get('grade') else questions
    except:
        return HttpResponseNotFound(f'<h1> Page not found because</h1>')
    
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)