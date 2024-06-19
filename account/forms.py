from django import forms
from django.contrib.auth.forms import UserChangeForm

from .models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput, label='Сыр сөз')
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput, label='Сыр сөздү ырастоо')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password', 'password_confirmation', 'image']
        labels = {
            'username': 'Колдонуучу аты',
            'first_name': 'Аты',
            'last_name': 'Фамилиясы',
            'email': 'Электрондук почта',
            'password': 'Сыр сөз',
            'password_confirmation': 'Сыр сөздү ырастоо',
            'image': 'Сүрөт',
        }
        help_texts = {
            'username': '25 символдон ашпаган, тамгалар, сандар жана атайын белгилерден @/./+/-/_ түзүлүш керек.',
        }
        error_messages = {
            'email': {
                'invalid': "е'мейл адрести туура жазыныз!",
            },
        }


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter (username=username).exists():
            raise forms.ValidationError('Бул колдонуучу аты бош эмес!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter (email=email).exists():
            raise forms.ValidationError("Бул е'мейл адреси колдонулган!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Сыр сөздөр дал келбейт!')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user

class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'image')