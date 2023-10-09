import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
import random

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f'Name: {self.name}; Age: {self.age}'

def index(request):
    context = {
        'title': 'softUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student_infoo': Student('Doncho', 19),
        'student': Student('Doncho', 19),
        'now': datetime.datetime.now,
        'students': [
            'Pesho',
            'Pesho',
            'Gosho',
            'Maria',
            'Stamat',
        ],
        # 'students': [],
        'values': list(range(20))
    }

    return render(request, 'index.html', context)

def redirect_to_home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')