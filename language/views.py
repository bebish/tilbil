from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Level, Language
from lesson.models import Lesson

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


class LevelView(ListView):
    model = Level
    template_name = 'level-list.html'
    context_object_name = "levels"


class LevelDetailView(DetailView):
    model = Level
    template_name = 'index.html'
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        level = kwargs['object'].id
        context['lessons'] = Lesson.objects.filter(level_id = level)
        return context
