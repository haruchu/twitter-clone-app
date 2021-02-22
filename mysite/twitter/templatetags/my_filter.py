from django.template.defaultfilters import register
from django import template

register = template.Library()

@register.filter
def is_any_userdata_exists(dictionary, value):
    for item in dictionary:
      if (item.user == value):
        return True
    return False

@register.filter
def is_any_tweetdata_exists(dictionary, value):
    for item in dictionary:
      if (item.tweet == value):
        return True
    return False
