from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm, ImageSizeLimitationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


class GoodsCreate(generic.CreateView):
    model = Goods
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = reverse_lazy('crud:goods_list')

    # def form_valid(self, form):
    #     goods = form.save()
    #     return redirect('crud:goods_detail', pk=goods.pk)


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods
    template_name = 'crud/goods_detail.html'


class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = reverse_lazy('crud:goods_create')

    # def get_success_url(self):
    #     # リダイレクト先が、データのidを埋め込むなど、動的になる場合は
    #     # このメソッドを上書きします。
    #
    #     # テンプレートファイルに渡している{{ goods }}と、同じもの(モデルインスタンス)
    #     # が、get_objectメソッドで取得できます
    #     goods = self.get_object()
    #     return reverse_lazy('crud:goods_detail', kwargs={'pk': goods.id})


class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = reverse_lazy('crud:goods_list')

    # 削除処理をするためにメソッド上書き
    def form_valid(self, form):
        # リダイレクト先のURLを取得
        success_url = self.get_success_url()
        # モデルインスタンス.フィールド名 = 値 で書き換えや代入ができる
        self.object.state_flag = False
        # saveメソッドでDBのレコードの更新や作成ができる
        self.object.save()
        # self.object.delete() # これが本来の削除処理
        return redirect(success_url)


class GoodsCreateWithImageSizeLimitation(generic.CreateView):
    form_class = ImageSizeLimitationForm
    template_name = 'crud/goods_create.html'
    success_url = reverse_lazy('crud:goods_list')


class CustomDeleteView(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.custom_delete()
        return HttpResponseRedirect(success_url)


