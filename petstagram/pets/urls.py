from django.urls import include, path

from pets.views import *


urlpatterns = [
    path('add/', CreatePetView.as_view(), name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', DetailsPetVIew.as_view(), name='details pet'),
        path('edit/', EditPetView.as_view(), name='edit pet'),
        path('delete/', DeletePetView.as_view(), name='delete pet'),
    ]))
]
