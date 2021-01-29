from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView,UserCreateView,HomeView

app_name = 'twitter'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('home/', HomeView.as_view(), name='home'),
]
