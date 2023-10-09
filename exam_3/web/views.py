from django.shortcuts import render, redirect

from web.forms import ProfileCreateForm, CarCreateForm, CarDetailsForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_all_cars():
    try:
        return Car.objects.all()
    except Car.DoesNotExist:
        return None


def get_price_of_all_cars():
    cars = get_all_cars()
    total_price = sum([x.price for x in cars])

    return total_price


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def catalogue(request):
    cars = get_all_cars()

    context = {
        'cars': cars,
    }

    return render(request, 'catalogue.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def get_car_by_pk(pk):
    try:
        return Car.objects.filter(pk=pk).get()
    except Car.DoesNotExist:
        return None


def car_details(request, pk):
    car = get_car_by_pk(pk)

    context = {
        'car': car,
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = get_car_by_pk(pk)
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-edit.html', context)


def profile_details(request):
    profile = get_profile()
    price = get_price_of_all_cars()

    context = {
        'profile': profile,
        'price': price,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)


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

    return render(request, 'profile/profile-edit.html', context)


def car_delete(request, pk):
    car = get_car_by_pk(pk)
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-delete.html', context)


def profile_delete(request):
    profile = get_profile()
    form = ProfileDeleteForm(instance=profile)
    if request.method == 'GET':
        pass
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)
