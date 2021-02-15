# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default="")
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text


