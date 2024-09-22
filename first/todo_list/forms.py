# forms.py
from django import forms
from .models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'deadline']

    description = forms.CharField(required=False)


class UpdateCardForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('description', 'deadline')
