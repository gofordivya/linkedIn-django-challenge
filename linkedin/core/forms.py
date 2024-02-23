from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError(
            'Name and job title should not contain numbers.')
    
class UserProfileForm(forms.ModelForm):
    job_title = forms.CharField(
        max_length=255,
        validators=[validate_no_numbers],
        error_messages={
            'min_length': 'Job title should be at least 14 characters long.'}
    )

class SignupForm(UserCreationForm):
    jobtitle = forms.CharField(max_length=255, required=True,
                                validators=[validate_no_numbers],
                                error_messages={
                                    'min_length': 'Job title should be at least 14 characters long.'
                                })

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'alert alert-danger'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'alert alert-danger'
    }))
