from typing import Any
from django.views.generic import ListView, DetailView

from .models import Level
from lesson.models import Lesson

# Create your views here.
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
