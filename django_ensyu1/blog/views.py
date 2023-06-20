from django.views.generic import CreateView, DetailView, UpdateView, FormView, ListView

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Article, Tag, Category
from .forms import TagCreateForm, ArticleCreateForm, ArticleUpdateForm


class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'


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
