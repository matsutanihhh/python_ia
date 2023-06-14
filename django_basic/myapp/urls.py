from django.urls import path
# 『.』は今いる場所（カレントディレクトリ）、
# ここでは from myapp import views でも可能
from . import views

app_name = 'myapp'

# urlpatternsという変数名を書き間違えるとエラー出る
# urls.pyは自分で作るファイル名なのでつづりミスに要注意
urlpatterns = [
    # どのurlでどのビューを呼ぶかを登録する
    # views.pyのhello関数を呼ぶ
    path('hello/', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('kome/', views.kome, name='kome'),
    # クラスビューの時のpathの記述の仕方
    # views.クラス名.as_view() と書く必要がある
    path('home3/', views.Home.as_view(), name='home3'),
    path('lesson/', views.lesson, name='lesson')
]
