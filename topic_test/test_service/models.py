from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class TestSuite(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('question-view', args=[str(self.id)])
        
    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    level = models.ForeignKey('TestSuite', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    level = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
