from django import forms
from .models import Tag, Article


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('name',)


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('title', 'text', 'tags', 'category')
