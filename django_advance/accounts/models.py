from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    # Userモデルの元々あるが、ユニークにしたいのでemailフィールドを上書き
    email = models.EmailField('メールアドレス', unique=True, null=True)

    # Userモデルにないフィールドの追加
    age = models.PositiveIntegerField('年齢', blank=True, null=True)

    REQUIRED_FIELDS = ['email', 'age']


# Django開発でよくあるパターン
# カスタムユーザーモデルを使うが、passとして定義だけしておく
# 将来的な変更に備えて、カスタムユーザーモデルを定義するだけしておく場合もある
# passとしているので、中身は普通のUserモデルと同じだが
# 途中からデフォルトユーザー→カスタムユーザー に変更する操作がないので、
# エラーなどが起きにくい
# class CustomUser(AbstractUser):
#     pass
