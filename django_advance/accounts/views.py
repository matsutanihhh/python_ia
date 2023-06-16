from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class AccountCreateView(generic.CreateView):
    Model = User
    form_class = UserCreationForm # ユーザー作成するために提供されているフォーム
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')
