"""
Djangoのクラスベース汎用ビューの中身を、
簡潔にまとめたファイルです。
特に使用頻度の高いメソッドを中身に記載しています。

各クラスベースビューが何をしているか、どういう処理の流れなのかを
確認するのに使ってください。
"""

from django.shortcuts import render, redirect


class TemplateView:
    template_name = None

    def get(self, request, *args, **kwargs):
        # GETリクエストのときに必ず呼ばれる
        # URLを直接入力してエンターしたとき
        # リンククリック時に、GETリクエスト
        context = self.get_context_data()
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        # てんプレートファイルに渡す辞書を作るメソッド
        context = {}
        return context


class ListView(TemplateView):
    model = None
    queryset = None
    template_name = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        context['object_list'] = self.get_queryset()
        context['モデル名小文字_list'] = self.get_queryset()
        return context

    def get_queryset(self):
        # データのリストを返すメソッド

        # class属性querysetがあれば、それを返す
        if self.queryset:
            return self.queryset

        # queryset属性がない場合は、モデル名.objects.all()を返す
        else:
            # モデル名.objects.all() とすると、DBから全てのデータを取得する
            # [モデルインスタンス1, モデルインスタンス2, ...]
            queryset = self.model.objects.all()
            return queryset


class DetailView(TemplateView):
    model = None
    template_name = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        context['object'] = self.get_object()
        context['モデル名小文字'] = self.get_object()
        return context

    def get_object(self):
        # URL内の<int:pk>を取り出している
        pk = self.kwargs['pk']

        # モデル名.objects.get(フィールド名=値)
        object = self.model.objects.get(pk=pk)
        return object


class FormView(TemplateView):
    form_class = None
    success_url = None
    template_name = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(self.request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        context['form'] = self.get_form()
        return context

    def get_form(self):
        if self.request.method == 'POST':
            form = self.form_class(self.request.POST)
            # form = ProductForm(self.request.POST)
        else:
            form = self.form_class()
            # form = ProductForm()
        return form

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # 入力内容に問題がなければ、is_validがTrue
        if form.is_valid():
            # 問題がなければ、form_validが呼ばれる
            return self.form_valid(form)
        else:
            # 問題あり
            return self.form_invalid(form)

    def form_valid(self, form):
        # FormViewでは、ほぼ確実にこのメソッドを上書きして
        # ここに追加の処理
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        context = self.get_context_data()
        # 結果的に、
        # context['form'] = ProductForm(self.request.POST)
        # みたいになる
        context['form'] = form
        return render(self.request, self.template_name, context)

    def get_success_url(self):
        # リダイレクト先のURLが動的な場合は、ここを上書き
        # データ作成後に、詳細ページに行くなど(URLのpkの値は、データ毎に違うため)
        return self.success_url


class CreateView(FormView):

    def form_valid(self, form):
        # CreateViewは、必ずモデルフォームを使っている
        # モデルフォームは必ず、saveメソッドをもっている
        form.save()
        return super().form_valid(form)
