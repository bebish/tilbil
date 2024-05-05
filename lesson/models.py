from django.db import models
from django.contrib import admin

from language.models import Language


class Question(models.Model):
    question_text = models.TextField()
    correct_answer = models.TextField()
    var1 = models.TextField()
    var2 = models.TextField()
    var3 = models.TextField()

    def __str__(self) -> str:
        return self.question_text

class Lesson(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=60)
    tests = models.ManyToManyField(Question, related_name='lessons')
    image = models.ImageField(upload_to='lessons',default='default_lesson.avif')

    def __str__(self) -> str:
        return self.name


class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ('tests',) 
