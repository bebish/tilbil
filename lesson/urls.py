from django.urls import path, include

from .views import LessonView, LessonDetailView

urlpatterns = [
    path('',LessonView.as_view(),name='lesson-view'),
    path('<int:pk>/',LessonDetailView.as_view(),name='lesson-detail-view'),

]