from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def hello(request):
    # HttpResponse関数は引数の文字列をwebページに引き渡す
    return HttpResponse('<h1>Hello</h1>')


def home(request):
    # render関数を使うとtemplatesフォルダ内のhtmlファイルを指定できる
    return render(request, 'myapp/home.html')


class Character:
    def __init__(self, name):
        self.name = name

    def greed(self):
        print(f'{self.name}：こんにちは！')


def home2(request):
    context = {
        'title': 'ホーム2です',
        'content1': 'おはよう',
        'content2': 'こんにちは',
        'content3': 'こんばんは',
        'taro': Character(name='taro')
    }
    # render関数の第3引数には辞書型データを入れることができる
    # この辞書型データは第2引数で指定したhtmlファイルに引き渡される
    return render(request, 'myapp/home2.html', context)


# TemplateViewは、HTMLを単純に表示するのに使う
class Home(generic.TemplateView):
    # 表示するテンプレートファイルの指定
    template_name = 'myapp/home2.html'

    # テンプレートファイルに追加で渡したいデータがある時は
    # このメソッドを呼び出す
    def get_context_data(self, **kwargs):
        # このメソッドを上書きするときは、毎回super()で親のメソッドを呼ぶ
        context = super().get_context_data(**kwargs)

        # 辞書[キー名] = 値　の形式で追加データを辞書に渡す
        context['title'] = 'ホーム2です'
        # 戻り値として辞書型データを返す
        return context


def kome(request):
    return render(request, 'myapp/kome.html')


def lesson(request):
    return render(request, 'myapp/lesson.html')
