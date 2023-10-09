# accounts urls.py

from django.urls import include, path

from accounts.views import *


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('edit/', edit_user, name='edit user'),
        path('delete/', delete_user, name='delete user'),
    ])),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password')
]
