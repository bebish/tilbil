from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages


from .forms import ProfileEditForm
from .forms import RegistrationForm
from .models import User

class RegistrationView(SuccessMessageMixin,CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    success_message = 'Cиз ийгиликтүү катталдыныз!'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password']
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(self.request, user)
        return response

class SignInView(LoginView):
    template_name = 'account/login.html'


def profile(request):
    return render(request, 'account/profile.html')
def logout_view(request):
    logout(request)
    return redirect('/')

class UserRatingView(ListView):
    model = User
    template_name = 'rating.html'
    context_object_name = 'users'

    def get_queryset(self):
        # Исключаем суперпользователей и сортируем остальных по рейтингу
        return User.objects.filter(is_superuser=False).order_by('-rating')

class UserWeekRatingView(ListView):
    model = User
    template_name = 'week-rating.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_superuser=False).order_by('-week_rating')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving changes
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'account/profile-edit.html', {'form': form})

# class DeleteAccountView(SuccessMessageMixin, DeleteView):
#     model = User
#     template_name = 'delete-account.html'
#     success_url = reverse_lazy('home')
#     success_message = 'Ийгиликтүү өчүрүлдү!'

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Ийгиликтүү өчүрүлдү!')
        logout(request)
        return redirect('home')

    return render(request, 'account/delete-account.html')