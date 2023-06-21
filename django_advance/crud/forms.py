from django import forms
from .models import Goods


class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')


class GoodsUpdateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')


class ImageSizeLimitationForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        # 画像がアップロードされていた場合
        if image:
            # ImageFieldとFileFieldには.sizeという属性がある
            if image.size > 10 * 1024: # 1kb = 1024byte
                # clean_メソッドで何かエラーを出す時は
                # raise forms.ValidationError('エラーメッセージ')
                raise forms.ValidationError("ファイルサイズが大きすぎます")
        return image

    def clean_name(self):
        name = self.cleaned_data.get('name', False)
        # NGワードが、商品名に含まれていないかチェック
        if 'NGワード' in name:
            raise forms.ValidationError("NGワードがふくまれていました")
        return name