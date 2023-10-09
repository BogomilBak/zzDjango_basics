
from django import forms
from django.core.validators import MinLengthValidator
from web.models import Person, Todo

from web.validators import validate_priority, validate_text


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
            MinLengthValidator(2),
        ),
        error_messages={
            'required': 'Todo text must be set!'
        }
    )

    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        validators=(
            validate_priority,
        ),
        required=False,
    )

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
    
    def clean(self):
        return super().clean()
    
    def clean_text(self):
        return self.cleaned_data['text'].lower()
    
    def clean_assignee(self):
        assignee = self.changed_data['assignee']
        if assignee.todo_set.count() > Todo.MAX_TODOS_COUNT_PER_PERSON:
            raise forms.ValidationError(f"{assignee} already has max todos")
        return assignee

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'