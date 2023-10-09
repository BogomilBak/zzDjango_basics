from django.db import models
from django.contrib.auth import models as auth_models

from accounts.managers import PetstagramUserManager


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()
