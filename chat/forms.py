from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'raw_responses']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name (optional)',
                'maxlength': 50
            }),
            'raw_responses': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your answer here (e.g. "pizza, sushi, salad")',
            }),
        }
        labels = {
            'raw_responses': ''
        }
