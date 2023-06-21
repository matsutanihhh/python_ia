from django import forms
from .models import GoodsGroup, CustomGoods


class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = GoodsGroup
        fields = ("name",) # 1要素なのでカンマをつける


class CustomGoodsCreationForm(forms.ModelForm):
    class Meta:
        model = CustomGoods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image', 'group')
