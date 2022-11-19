from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save(*args, **kwargs)