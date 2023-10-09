from django.urls import path

from web.views import department_details, index


urlpatterns = [
    path('', index, name='index'),
    path('department/<int:pk>', department_details, name='details department'),
]
