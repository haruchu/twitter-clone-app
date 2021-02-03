from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView,UserInputView,UserConfirmView,UserCreateView,HomeView

app_name = 'twitter'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('input/', UserInputView.as_view(), name='input'),
    path('confirm/', UserConfirmView.as_view(), name='confirm'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('home/', HomeView.as_view(), name='home'),
]