from django.shortcuts import render, redirect
from django.core import exceptions
from web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_albums():
    try:
        return Album.objects.all()
    except Album.DoesNotExist:
        return None


def get_album(pk):
    return Album.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('profile add')

    albums = get_albums()

    context = {
        'albums': albums,
    }

    return render(request, 'home/home-with-profile.html', context)


def album_add(request):
    if request.method == "GET":
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = get_album(pk)

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context)


def album_edit(request, pk):
    album = get_album(pk)
    if request.method == "GET":
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context)


def album_delete(request, pk):
    album = get_album(pk)
    if request.method == "GET":
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.count()
    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_add(request):
    if get_profile():
        return redirect('index')

    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'home/home-no-profile.html', context)


def profile_delete(request):
    current_profile = get_profile()
    form = DeleteProfileForm(instance=current_profile)
    if request.method == 'GET':
        pass
    else:
        form = DeleteProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': current_profile,
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)

