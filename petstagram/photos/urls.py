from django.urls import include, path

from photos.views import *


urlpatterns = [
    path('add/', CreatePetPhotoView.as_view(), name='add photo'),
    path('<int:pk>/', include([
        path('', PetPhotoDetailsView.as_view(), name='details photo'),
        path('edit/', edit_photo, name='edit photo'),
        path('delete/', delete_photo, name='delete photo'),
    ])), 
]
