from rest_framework import serializers
from .models import Question, AnswerOption, Subject

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'answer_text']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name']
# class HighlightedWordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HighlightedWord
#         fields = ['id', 'highlighted_text']

# class QuestionDiagramSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuestionDiagram
#         fields = ['id',         

class QuestionSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(many=True)
    subject = SubjectSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id', 'topic', 'subject', 'question_text', 'diagram_image', 'highlight', 'correct_answer_text', 'answer_options', 'grade', 'is_approved']    

