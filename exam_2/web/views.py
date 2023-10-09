from django.shortcuts import render, redirect

from web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from web.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'home/home-page.html', context)


def get_all_plants():
    try:
        return Plant.objects.all()
    except Plant.DoesNotExist:
        return None


def catalogue(request):
    plants = get_all_plants()

    context = {
        'plants': plants
    }

    return render(request, 'catalogue.html', context)


def plant_create(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'plants/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant
    }

    return render(request, 'plants/plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plants/edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plants/delete-plant.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    total_plants = Plant.objects.count()
    profile = Profile.objects.get()
    context = {
        'plants': total_plants,
        'profile': profile,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.get()
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
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'profile/delete-profile.html', context)

