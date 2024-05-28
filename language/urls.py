from django.urls import path,include

from .views import LevelView, LevelDetailView, home, LanguageView, LanguageDetailView

urlpatterns = [
    path('', home, name='home'),
    path('level/',LevelView.as_view(),name='level-view'),
    path('level/<int:pk>/',LevelDetailView.as_view(),name='level-detail-view'),
    path('language/', LanguageView.as_view(),name='language-list'),
    path('language/<int:pk>/', LanguageDetailView.as_view(),name='language-detail'),

]