from django.shortcuts import render, redirect

from web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from web.models import Profile, Fruit


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_all_fruits():
    try:
        return Fruit.objects.all()
    except Fruit.DoesNotExist:
        return None


def index(request):

    context = {
        'profile': get_profile(),
    }

    return render(request, 'index.html', context)


def dashboard(request):
    fruits = get_all_fruits()
    context = {
        'fruits': fruits,
        'profile': get_profile()
    }

    return render(request, 'dashboard.html', context)


def fruit_create(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):

    context = {
        'fruit': Fruit.objects.filter(pk=pk).get(),
        'profile': get_profile(),
    }

    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'fruit': fruit,
        'form': form,
    }

    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'fruit': fruit,
        'form': form,
    }
    return render(request, 'fruit/delete-fruit.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,

    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):

    context = {
        'profile': get_profile(),
        'fruits': Fruit.objects.count(),
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
        context = {
            'profile': profile,
            'form': form,
        }

        return render(request, 'profile/delete-profile.html', context)

    form = ProfileDeleteForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('index')





