from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from common.utils import get_user_liked_photos
from photos.forms import PhotoCreateForm, PhotoDeleteForm, PhotoEditForm

from photos.models import Photo


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    context = {
        'photo': photo,
        'has_user_liked': get_user_liked_photos(pk),
        'likes_count': photo.photolike_set.count(),

    }

    return render(request, 'photos/photo-details-page.html', context)


class PetPhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'
    context_object_name = 'pet_photo'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class CreatePetPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoCreateForm

    success_url = reverse_lazy('index')


def add_photo(request):
    if request.method == "GET":
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect('details photo', pk=photo.pk)
        
    context = {
        'form': form,
    }

    return render(request,'photos/photo-add-page.html', context)



def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = PhotoEditForm()
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect('details photo', pk=photo.pk)
        
    context = {
        'form': form,
        'pk': pk,
    }
    
    return render(request, 'photos/photo-edit-page.html', context)

def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = PhotoDeleteForm()
    else:
        form = PhotoDeleteForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect('index', pk=photo.pk)
        
    context = {
        'form': form,
        'pk': pk,
    }
    
    return render(request, 'photos/photo-delete-page.html', context)
