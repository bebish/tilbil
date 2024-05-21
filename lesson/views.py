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
        fill_in_the_blank_tests = lesson.fill_in_the_blank_tests.all()
        fill_in_the_blank_tests_data = [
            {
                'question_text': test.question_text,
                'correct_answer': test.correct_answer,
                'blank_words': test.blank_words.split(',')
            } for test in fill_in_the_blank_tests
        ]
        context['tests'] = tests
        context['fill_in_the_blank_tests'] = fill_in_the_blank_tests_data
        return context

    