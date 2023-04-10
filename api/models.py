from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    grade = models.ManyToManyField(Grade)

    def __str__(self):
        return self.name    

class Topic(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.TextField() 
    diagram_image = models.ImageField(upload_to='diagrams/', null=True, blank=True) 
    highlight = models.CharField(max_length=200, null=True, blank=True)
    correct_answer_text = models.TextField()
    grade = models.ManyToManyField(Grade)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text
    
class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_options')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_text
    
