from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView

from .models import *

# Create your views here.
class LessonView(ListView):
    model = Lesson
    template_name = 'index.html'
    context_object_name = 'lessons'

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson-detail.html'
    context_object_name = 'content'