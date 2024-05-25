from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm
from .models import User

class RegistrationView(SuccessMessageMixin,CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('lesson-view')
    success_message = 'Successfully registered'

class SignInView(LoginView):
    template_name = 'account/login.html'

def logout_view(request):
    logout(request)
    return redirect('/lesson')