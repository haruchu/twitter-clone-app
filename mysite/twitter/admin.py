from django.contrib import admin

# Register your models here.
from .models import Tweet, FriendShip

admin.site.register(Tweet)
admin.site.register(FriendShip)
