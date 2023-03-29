from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def name(self):
        return self.first_name+' '+self.last_name

    def __str__(self):
        return self.email


