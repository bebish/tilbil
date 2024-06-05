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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        level = self.get_object()
        categories = LessonCategory.objects.filter(lesson_level=level)
        lessons_by_category = {}

        # Получаем список завершенных уроков для текущего пользователя
        completed_lessons = set(self.request.user.completed_lessons)

        for category in categories:
            # Получаем все уроки для каждой категории
            lessons = category.lessons.all()

            # Добавляем атрибут `is_completed` к каждому уроку
            for lesson in lessons:
                lesson.is_completed = lesson.id in completed_lessons

            lessons_by_category[category] = lessons

        context['categories_with_lessons'] = lessons_by_category
        return context
