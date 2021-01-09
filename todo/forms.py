from django import forms
from todo.models import Todo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields= [
            'task_name',
            'task_desc',
            'status',
            'priority',
            'due_date',
        ]