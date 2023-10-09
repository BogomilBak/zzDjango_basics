from django.urls import path
from web.views import create_person, index, list_persons


urlpatterns = [
    path('', index, name='index'),
    path('persons/', list_persons, name='list persons'),
    path('create/', create_person, name='create person'),
]
