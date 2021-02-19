from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView, UserInputView, UserConfirmView, UserCreateView, HomeView, CreateTweet, ProfileView, follow_view, unfollow_view,like

app_name = 'twitter'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('input/', UserInputView.as_view(), name='input'),
    path('confirm/', UserConfirmView.as_view(), name='confirm'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('home/', HomeView.as_view(), name='home'),
    path('tweet/', CreateTweet.as_view(), name='tweet'),
    path("<int:pk>/like/",like,name="like"),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/follow', follow_view, name='follow'),
    path('profile/<int:pk>/unfollow', unfollow_view, name='unfollow'),
]
