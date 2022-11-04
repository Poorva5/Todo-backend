from django.db import models
from django.contrib.auth.models import User

class TaskData(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title