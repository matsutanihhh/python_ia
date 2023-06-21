from django import forms
from .models import CorporateContact
from django.views import generic


class CorporateContactForm(forms.ModelForm):
    class Meta:
        model = CorporateContact
        # '__all__' とすると、全ての入力欄になります
        fields = '__all__'
