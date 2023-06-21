from django import forms
from .models import CorporateContact, IndividualContact
from django.views import generic


class CorporateContactForm(forms.ModelForm):
    class Meta:
        model = CorporateContact
        # '__all__' とすると、全ての入力欄になります
        fields = '__all__'


class IndividualContactForm(forms.ModelForm):
    class Meta:
        model = IndividualContact
        # '__all__' とすると、全ての入力欄になります
        fields = '__all__'
