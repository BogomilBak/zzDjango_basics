from django.urls import path

from web.views import index, index_model_form


urlpatterns = [
    path('', index, name='index'),
    path('modelforms/', index_model_form, name='model forms')
]
