from django import forms
# from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    # just get rid of the label and add some placeholder
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task title...'}), label=False)
    due = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Due date...'}), label=False)

    class Meta:
        model = Task
        fields = ['title', 'due']


class UpdateTaskForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task title...'}))

    class Meta:
        model = Task
        fields = ['title', 'due', 'is_complete']