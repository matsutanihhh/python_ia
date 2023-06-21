from django.urls import path
from .views import *

app_name = 'contacts'
urlpatterns = [
    path('', CorporateContactInput.as_view(), name='corporate_input'),
    path('corporate_confirm/', CorporateContactConfirm.as_view(), name='corporate_confirm'),
    path('corporate_create/', CorporateContactCreate.as_view(), name='corporate_create'),
    path('form_send_complete/', FormSendComplete.as_view(), name='form_send_complete'),
]