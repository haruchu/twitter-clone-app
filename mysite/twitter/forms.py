from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    text = forms.CharField(max_length=100)
    class Meta:
        model = Tweet
        fields = ("text",)
