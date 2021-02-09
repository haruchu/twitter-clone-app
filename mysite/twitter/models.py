# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text


