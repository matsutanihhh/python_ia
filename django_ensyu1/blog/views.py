from django.views.generic import CreateView, DetailView, UpdateView, FormView, ListView

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Article, Tag, Category, Comment
from .forms import TagCreateForm, ArticleCreateForm, ArticleUpdateForm, SearchForm, CommentCreateForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect


class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'

    # 並び替えをする order_by('フィールド名') デフォルトは昇順
    # order_by('-フィールド名') 『-』をつけると降順
    queryset = Article.objects.all().order_by('-created_at')

    # 選択肢となるデータの一覧

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        # 絞り込みのために上書き
        queryset = super().get_queryset()  # .order_by('-created_at') #ここで並び替えを書いてもいい

        # GETパラメータを、フォームに紐づける
        form = SearchForm(self.request.GET)
        form.is_valid()  # フォームからデータを取り出すのに必要な行

        # 値 = フォームオブジェクト.cleaned_data.get('フォームオブジェクトのフィールド名')
        keyword = form.cleaned_data.get('keyword')
        # management_code = form.cleaned_data.get('management_code')
        # price_begin = form.cleaned_data.get('price_begin')
        # price_end = form.cleaned_data.get('price_end')
        # group = form.cleaned_data.get('group')

        if keyword:
            # .filter(モデルオブジェクトのフィールド名=値)
            # queryset = queryset.filter(title__icontains=keyword)
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )

        # if management_code:
        #     queryset = queryset.filter(management_code=management_code)
        # if group:
        #     queryset = queryset.filter(group=group)
        # if price_begin:
        #     # filter(フィールド名__特殊条件=値)
        #     # gte greater than equal >=のこと
        #     queryset = queryset.filter(price__gte=price_begin)
        # if price_end:
        #     queryset = queryset.filter(price__lte=price_end)
        return queryset


class TagListView(ListView):
    model = Tag
    template_name = 'blog/tag_list.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    # DetailViewがもともと持っている、get_objectメソッドの紹介。
    # データベースから、1つのデータを取得する

    def get_object(self, queryset=None):
        # self.kwargsは、URL内の int:pkといった部分が入っている
        article = Article.objects.get(pk=self.kwargs['pk'])
        # →Staff.objects.get(pk=1)  # 今回、URLは/staff_detail/1/
        # →Staff.objects.get(id=1)  # pkというのは、primarykeyのこと。今回ならidフィールドのこと
        # print(staff.name) # ここで書くとターミナルに表示される
        return article

    def get_context_data(self, **kwargs):
        # contextは取ってこなければならない
        # 新しく作るとstaffに入ったデータが取ってこられない
        context = super().get_context_data(**kwargs)
        # DetailViewにはget_objectメソッドがあり
        # URLのidを元にモデルのインスタンスを取得している
        article = self.get_object()
        tags = article.tags.all()
        context['books'] = tags
        return context


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:article_list')  # テンプレートで使った、urlタグみたいなもの
    form_class = TagCreateForm


class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:article_list')  # テンプレートで使った、urlタグみたいなもの
    form_class = ArticleCreateForm


class ArticleUpdateView(generic.UpdateView):
    model = Article
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = ArticleUpdateForm


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article_list')


class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = CommentCreateForm

    def form_valid(self, form):
        # form.save(commit=False) データベースにはまだ保存しない
        # commit=False　ビューでモデルのフィールドを埋めるために使う引数
        comment = form.save(commit=False)

        # commentモデルのtargetフィールドをここで埋める
        # モデル名.objects.get(フィールド=値) 1つだけDBから取り出すのに使うメソッドがget
        # url内の<int:pk>はself.kwargs['pk']で取得できる
        comment.target = Article.objects.get(pk=self.kwargs['pk'])

        # 上2行をまとめてこう書かれている場合も多い
        # form.instance.target = Article.objects.get(pk=self.kwargs['pk'])

        comment.save()
        return redirect('blog:article_list')
