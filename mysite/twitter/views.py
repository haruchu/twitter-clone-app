from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormView
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

class HomeView(LoginRequiredMixin,generic.FormView) :
    template_name = "twitter/home.html"
    form_class = TweetForm
    login_url = '/'
    def get_context_data(self, **kwargs):
        initial_dict = {'user': self.request.user}
        form_class = TweetForm(self.request.POST or None, initial=initial_dict)
        # TemplateViewにあるcontextを取得
        context = super().get_context_data(**kwargs)
        # contextにformというキーでformという変数を追加
        context["form"] = form_class
        # contextにtweetsというキーでツイート一覧を追加
        context["tweets"] = Tweet.objects.all()
        return context

class CreateTweet(generic.FormView):
        success_url = reverse_lazy('twitter:home')
        form_class = TweetForm
        def form_valid(self, form):
            form_class = TweetForm(self.request.POST)
            post = form_class.save(commit=False)
            post.user = self.request.user
            post = form.save()
            return redirect('twitter:home')
        def form_invalid(self, form):
            return render(self.request, 'twitter/home.html', {'form': form})





