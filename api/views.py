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
        topic_name = request.GET.get('topic')
        subject_name = request.GET.get('subject')
        grade_name = request.GET.get('grade')
        limit = request.GET.get('limit')
        questions = questions.filter(topic__name=topic_name) if topic_name else questions
        questions = questions.filter(grade__name=grade_name) if grade_name else questions
        questions = questions.filter(subject__name=subject_name) if subject_name else questions
        questions = questions[:int(limit)] if limit else questions

    except:
        return HttpResponseNotFound(f'<h1> Page not found</h1>')
    
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)