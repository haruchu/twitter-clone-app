# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser




class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default="")
    text = models.CharField(max_length=200)
    # slug = models.SlugField(null=False, unique=True,default=some_method())
    # def __str__(self):
    #     return self.text

    # def get_absolute_url(self):
    #     return reverse('user_detail', kwargs={'slug': self.slug})


class User(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('twitter:profile', kwargs={'username': self.user.username})
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.user)
    #     return super().save(*args, **kwargs)
