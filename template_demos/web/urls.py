from django.urls import path

from web.views import about, index, redirect_to_home


urlpatterns = [
    path('', index, name='index'),
    path('go-to-home', redirect_to_home, name='redirect to home'),
    path('about/', about, name='about')
]
