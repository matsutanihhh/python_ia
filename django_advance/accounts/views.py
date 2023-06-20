from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class AccountCreateView(generic.CreateView):
    # model = User
    model = CustomUser
    # form_class = UserCreationForm # ユーザー作成するために提供されているフォーム
    form_class = MyUserCreationForm # 新しく作ったクラスを指定
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    # next_page = '/accounts/login'
    # ログアウト後に遷移するページ
    next_page = reverse_lazy('accounts:login')


class Home(TemplateView):
    template_name = 'accounts/home.html'

