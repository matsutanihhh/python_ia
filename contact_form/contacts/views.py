from django.views import generic
from django.urls import reverse_lazy
from .forms import CorporateContactForm, IndividualContactForm
from .models import CorporateContact, IndividualContact

from django.template.loader import get_template
from accounts.models import CustomUser
from django.shortcuts import redirect, render


# 確認画面を作る時
# 1. FormViewで、入力欄のあるページを作る CorporateContactInput
# 2. FormViewで、入力内容を表示する確認ページを作る CorporateContactConfirm
# 3. CreateViewで、入力内容を保存するビューを作る CorporateContactCreate

# CreateViewから、データの保存処理をなくしたビューがFormView
class CorporateContactInput(generic.FormView):
    """確認画面機能の、最初の入力ページ"""
    form_class = CorporateContactForm
    template_name = 'contacts/corporate_contact_input.html'

    def form_valid(self, form):
        # 確認画面、戻るボタンを押したときに呼ばれる
        context = {
            'form': form,  # input type="hidden" で隠れていたデータが、ちゃんとはいってます
        }
        return render(
            self.request,
            'contacts/corporate_contact_input.html',
            context
        )


class IndividualContactInput(generic.FormView):
    """確認画面機能の、最初の入力ページ"""
    form_class = IndividualContactForm
    template_name = 'contacts/individual_contact_input.html'

    def form_valid(self, form):
        # 確認画面、戻るボタンを押したときに呼ばれる
        context = {
            'form': form,  # input type="hidden" で隠れていたデータが、ちゃんとはいってます
        }
        return render(
            self.request,
            'contacts/individual_contact_input.html',
            context
        )


class CorporateContactConfirm(generic.FormView):
    form_class = CorporateContactForm

    def form_valid(self, form):
        # 入力ページ (/) で、送信を押すと呼ばれる
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/corporate_contact_confirm.html',
            context
        )

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/corporate_contact_confirm.html',
            context
        )


class IndividualContactConfirm(generic.FormView):
    form_class = IndividualContactForm

    def form_valid(self, form):
        # 入力ページ (/) で、送信を押すと呼ばれる
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/individual_contact_confirm.html',
            context
        )

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/individual_contact_confirm.html',
            context
        )


class CorporateContactCreate(generic.CreateView):
    model = CorporateContact
    form_class = CorporateContactForm
    success_url = reverse_lazy('contacts:form_send_complete')

    def form_invalid(self, form):
        # 確認画面で、送信ボタンを押したが、入力内容が悪かった
        # 本来呼ばれないはず
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/corporate_contact_input.html',
            context
        )

    def form_valid(self, form):
        # 確認画面で、送信を押すと呼ばれる

        # モデルフォームのsaveメソッドで、DBに保存される
        # saveメソッドは、モデルインスタンスを返す
        corporate = form.save()

        # テンプレートファイルに、辞書を渡して、メール本文の文字列を作成している
        subject = '題名'
        mail_text_template = get_template('contacts/email/corporate_message.txt')
        context = {
            'corporate': corporate,
        }
        # mail_textには、メールの本文が文字列で作られた状態
        mail_text = mail_text_template.render(context)

        # メールの送信処理
        # モデル名.objects.filter(フィールド名=値)で、絞り込むことができます
        for user in CustomUser.objects.filter(is_received_email=True):
            # 実際にメールを送る。Userモデルに定義されている、メール送信用のメソッド
            user.email_user(subject, mail_text, 'info@a.com')

        return redirect('contacts:form_send_complete')


class IndividualContactCreate(generic.CreateView):
    model = IndividualContact
    form_class = IndividualContactForm
    success_url = reverse_lazy('contacts:form_send_complete')

    def form_invalid(self, form):
        # 確認画面で、送信ボタンを押したが、入力内容が悪かった
        # 本来呼ばれないはず
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/individual_contact_input.html',
            context
        )

    def form_valid(self, form):
        # 確認画面で、送信を押すと呼ばれる

        # モデルフォームのsaveメソッドで、DBに保存される
        # saveメソッドは、モデルインスタンスを返す
        individual = form.save()

        # テンプレートファイルに、辞書を渡して、メール本文の文字列を作成している
        subject = '題名'
        mail_text_template = get_template('contacts/email/individual_message.txt')
        context = {
            'individual': individual,
        }
        # mail_textには、メールの本文が文字列で作られた状態
        mail_text = mail_text_template.render(context)

        # メールの送信処理
        # モデル名.objects.filter(フィールド名=値)で、絞り込むことができます
        for user in CustomUser.objects.filter(is_received_email=True):
            # 実際にメールを送る。Userモデルに定義されている、メール送信用のメソッド
            user.email_user(subject, mail_text, 'info@a.com')

        return redirect('contacts:form_send_complete')


class FormSendComplete(generic.TemplateView):
    template_name = 'contacts/form_send_complete.html'
