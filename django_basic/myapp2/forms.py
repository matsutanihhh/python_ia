from django import forms
from .models import StaffInformation, Department, Book, Staff


# ModelFormを継承することで簡単に入力フォームが作れる
class StaffInformationForm(forms.ModelForm):
    # Djangoでは class Meta: というものを定義する
    class Meta:
        model = StaffInformation
        # fieldsは画面上に表示する入力欄と対応している
        # #フィールド全て
        # fields = "__all__"
        #
        # #フィールドの一部
        # fields = ["フィールド1", "フィールド2"]
        #
        # #一部のフィールドを除く
        # exclude = "除きたいフィールド"
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'management_code')


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'information', 'department', 'rented_books')


class StaffInformationUpdateForm(forms.ModelForm):
    class Meta:
        model = StaffInformation
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')
