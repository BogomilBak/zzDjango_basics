from django.http import HttpResponse
from django.shortcuts import redirect, render
from web.forms import PersonCreateForm, TodoCreateForm, TodoForm
from web.models import Person


def index(request):
    if request.method == "GET":
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            model = form.instance
            model.full_clean()
            return HttpResponse("All is valid")
        
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

def list_persons(request):
    context = {
        'persons': Person.objects.all()
    }

    return render(request, 'list-person.html', context)

def create_person(request):
    if request.method == "GET":
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list persons')

    context = {
        'form': form
    }

    return render(request, 'create-person.html', context)


