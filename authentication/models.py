from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .manager import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):

    class Roles(models.TextChoices):
        ADMIN = 'A', _('admin')
        RAPPER = 'R', _('rapper')
        ORGANIZER = 'O', _('competition organizer')
        NORMAL = 'N', _('normal')

    email = models.EmailField(max_length=100, unique=True)

    role = models.CharField(max_length=1, choices=Roles.choices)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AccountManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perm(self, add_label):
        return self.is_superuser


class Profile(models.Model):
    """
        Profile model associated with User's Account model
    """
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name="profile_account")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    awards = models.CharField(max_length=255, null=True)
    trophies = models.CharField(max_length=255, null=True)
    social_links = models.JSONField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
