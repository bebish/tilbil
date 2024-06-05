from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, DeleteView
from django.utils import timezone

from .models import *
from .forms import TranslateQuestionForm
from account.models import User


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson-detail.html'
    context_object_name = 'lesson'

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.get_object()
        user = self.request.user
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
        listen_tests = lesson.listen_tests.all()
        listen_tests_data = [
            {
                'question_text': test.question_text,
                'correct_answer': test.correct_answer,
                'blank_words': test.blank_words.split(',')
            } for test in listen_tests
        ]

        context['tests'] = tests
        context['fill_in_the_blank_tests'] = fill_in_the_blank_tests_data
        context['translate_tests'] = translate_tests
        context['translate_form'] = TranslateQuestionForm()
        context['listen_tests'] = listen_tests_data

        if 'user_answer' in self.request.POST:
            context['user_answer'] = self.request.POST.get('user_answer')

        user.save()

        return context

    def get(self, request, *args, **kwargs):
        lesson = self.get_object()
        user = request.user

        if lesson.id not in user.completed_lessons:
            user.completed_lessons.append(lesson.id)
            user.rating += 20
        else:
            user.rating += 5

        user.save()

        return super().get(request, *args, **kwargs)

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
    
class CategoryDetailView(DeleteView):
    model = LessonCategory
    template_name = 'category-detail.html'
    context_object_name = 'category'

