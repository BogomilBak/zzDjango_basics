from django import forms
from django.shortcuts import render

from web.models import Person

class PersonForm(forms.Form):
    OCCUPANCIES = (
        ('1,', 'Child'),
        ('2', 'High school student'),
        ('3', 'Student'),
        ('4', 'Adult'),
        ('5', 'Old person'),
    )


    your_name = forms.CharField(
        max_length=30,
        label='name',
        help_text='enter your name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            }
        )
    )
    age = forms.IntegerField(
        initial=0,
        required=False,
        widget=forms.NumberInput(),
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
    )

    story = forms.CharField(
        widget=forms.Textarea(),
    )

    url = forms.CharField(
        widget=forms.URLInput(),
    )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
    )
    
    occupancy2 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect(),
    )


def index(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
        Person.objects.create(
            name=name,
        )
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

def index_model_form(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST)
        if form.isvalid():
            print(form.cleaned_data)

    context = {
        'form': form,
    }
    return render(request, 'model_forms.html', context)