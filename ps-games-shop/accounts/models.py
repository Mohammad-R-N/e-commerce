from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser,PermissionsMixin):
    
    username = models.CharField(max_length=100,verbose_name=_("User Name"))
    email = models.EmailField(unique=True,verbose_name=_("Email"))
    password = models.CharField(max_length=18,verbose_name=_("Password"))
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True, editable=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username