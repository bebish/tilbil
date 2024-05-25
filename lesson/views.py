from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView

from .models import *
from .forms import TranslateQuestionForm

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
        translate_tests = lesson.translate_tests.all()
        context['tests'] = tests
        context['fill_in_the_blank_tests'] = fill_in_the_blank_tests_data
        context['translate_tests']=translate_tests
        context['translate_form'] = TranslateQuestionForm()

        # Если есть ответ пользователя в запросе, добавляем его в контекст
        if 'user_answer' in self.request.POST:
            context['user_answer'] = self.request.POST.get('user_answer')

        return context

    def post(self, request, *args, **kwargs):
        lesson = self.get_object()
        translate_form = TranslateQuestionForm(request.POST)
        if translate_form.is_valid():
            # Получаем и сохраняем ответ пользователя
            user_answer = translate_form.cleaned_data['user_answer']

            # Сохраняем ответ пользователя в запросе для передачи в контекст
            request.POST = request.POST.copy()
            request.POST['user_answer'] = user_answer

        # После обработки ответа можно выполнить редирект на ту же страницу
        return HttpResponseRedirect(reverse('lesson-detail', args=(lesson.pk,)))