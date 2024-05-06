from typing import Any
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
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.get_object()
        tests = lesson.tests.all()
        context['tests'] = tests
        return context
    