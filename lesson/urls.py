from django.urls import path, include

from .views import LessonDetailView

urlpatterns = [
    path('<int:pk>/',LessonDetailView.as_view(),name='lesson-detail-view'),
]