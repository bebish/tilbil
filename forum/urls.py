from django.urls import path

from .views import *

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', topic_list, name='topic_list'),
    path('category/<int:category_id>/topic/<int:topic_id>/', post_list, name='post_list'),
    path('category/<int:category_id>/create_topic/', create_topic, name='create_topic'),
    path('category/<int:category_id>/topic/<int:topic_id>/create_post/', create_post, name='create_post'),
]