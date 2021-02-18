from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '40', 'rows': '5', 'max_length': '200'}))

    class Meta:
        model = Tweet
        fields = ("user", "text")
