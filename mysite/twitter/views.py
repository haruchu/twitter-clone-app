from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import TweetForm
from .models import Tweet


class IndexView(generic.TemplateView):
    template_name = "twitter/signup.html"

# Create your views here.

class UserInputView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'twitter/input.html'
    def form_valid(self, form):
        return render(self.request, 'twitter/input.html', {'form': form})

class UserConfirmView(generic.FormView):
    form_class = UserCreationForm
    def form_valid(self, form):
        return render(self.request, 'twitter/confirm.html', {'form': form})
    def form_invalid(self, form):
        return render(self.request, 'twitter/input.html', {'form': form})

class UserCreateView(generic.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('twitter:home')
    def form_valid(self, form):
        # 認証
        user = form.save()
        # ログイン
        login(self.request, user)
        return super().form_valid(form)
    def form_invalid(self, form):
        return render(self.request, 'twitter/input.html', {'form': form})

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = "twitter/home.html"
    login_url = '/'
    def home(request):
        model = Tweet.objects.values()
        form = TweetForm(request.POST)
        context = {'model': model, 'form': form}
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect("home")
            else:
                return redirect("home")
        else:
            form = TweetForm()
        return render(request, 'Twitter/home.html', context)


