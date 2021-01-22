from django.urls import path

from .views import IndexView,UserCreateView,HomeView

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('home/', HomeView.as_view(), name='home'),
]
