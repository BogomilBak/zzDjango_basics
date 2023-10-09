from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy


def login_user(request):
    return render(request, 'accounts/login-page.html')

def register_user(request):
    return render(request, 'accounts/register-page.html')

def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')

def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')

def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


class UserRegisterView():
    pass


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        # if self.get_success_url():
        #     return self.success_url
        return super().get_success_url()


class UserDetailsView:
    pass


class EditProfileVIew:
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    pass


