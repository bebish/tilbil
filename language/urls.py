from django.urls import path

from .views import LevelDetailView, home, LanguageView, LanguageDetailView
from lesson.views import CategoryDetailView

urlpatterns = [
    path('', home, name='home'),
    path('level/<int:pk>/',LevelDetailView.as_view(),name='level-detail-view'),
    path('language/', LanguageView.as_view(),name='language-list'),
    path('language/<int:pk>/', LanguageDetailView.as_view(),name='language-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(),name='category-detail'),

]