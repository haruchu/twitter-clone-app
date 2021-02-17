# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default="")
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text

class FriendShip(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee_friendships')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_friendships')
    class Meta:
        unique_together = ('follower', 'followee')
    def __str__(self):
        return (self.follower,"⇔",self.followee)



