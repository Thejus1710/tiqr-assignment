from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="colabs")
    def __str__(self):
        return self.creator.username