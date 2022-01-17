from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todo_manager_app.models import Todo


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# class SignUpForm()

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'due_date', 'attachment', 'status_done']

    # status_done = forms.BooleanField(widget=forms.CheckboxInput)
