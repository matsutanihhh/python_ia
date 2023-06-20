from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class MyUserCreationForm(UserCreationForm):
    # UserCreationFormはモデルフォームとして作られている
    # class Metaの部分を自分で上書きする
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'is_active', 'age', 'email')
