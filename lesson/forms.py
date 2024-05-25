from django import forms
from .models import TranslateQuestion

class TranslateQuestionForm(forms.ModelForm):
    class Meta:
        model = TranslateQuestion
        fields = ['user_answer']
        widgets = {
            'user_answer': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
