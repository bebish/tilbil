from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Level, Language
from lesson.models import Lesson, LessonCategory

def home(request):
    return render(request, 'home.html')

# Create your views here.
class LanguageView(ListView):
    model = Language
    template_name = 'select-language.html'
    context_object_name = 'languages'

class LanguageDetailView(DetailView):
    model = Language
    template_name = 'level-list.html'
    context_object_name = 'levels'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        language = kwargs['object'].id
        context['levels'] = Level.objects.filter(language_id = language)
        return context


class LevelDetailView(DetailView):
    model = Level
    template_name = 'index.html'
    context_object_name = 'level'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        level = self.get_object()  # Получаем объект уровня
        categories = LessonCategory.objects.filter(lesson_level=level)  # Получаем все категории для данного уровня
        lessons_by_category = {}  # Создаем словарь для хранения уроков по категориям
        for category in categories:
            lessons_by_category[category] = category.lessons.all()  # Получаем все уроки для каждой категории
        context['categories_with_lessons'] = lessons_by_category  # Передаем словарь с категориями и уроками в контекст
        return context
