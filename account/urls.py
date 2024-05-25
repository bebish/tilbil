from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # path('myprofile/', profile, name='profile'),
]