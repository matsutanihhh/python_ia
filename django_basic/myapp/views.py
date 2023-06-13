from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # HttpResponse関数は引数の文字列をwebページに引き渡す
    return HttpResponse('<h1>Hello</h1>')


def home(request):
    # render関数を使うとtemplatesフォルダ内のhtmlファイルを指定できる
    return render(request, 'myapp/home.html')
