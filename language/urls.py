from django.urls import path,include

from .views import LevelView, LevelDetailView

urlpatterns = [
    path('level',LevelView.as_view(),name='level-view'),
    path('level/<int:pk>/',LevelDetailView.as_view(),name='level-detail-view')
]