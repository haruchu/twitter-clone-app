from django.contrib import admin

# Register your models here.
from .models import Tweet, FriendShip, Like

admin.site.register(Tweet)
admin.site.register(FriendShip)
admin.site.register(Like)
