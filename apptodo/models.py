from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class todotask(models.Model):
    choi = [
    ("low", "low"),
    ("moderate", "moderate"),
    ("high", "high"),
]
    username = models.CharField(max_length=20)
    Task = models.CharField(max_length=100)
    starts = models.DateField()
    ends = models.DateField()
    priority = models.CharField(choices= choi, max_length=10)

    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.Task