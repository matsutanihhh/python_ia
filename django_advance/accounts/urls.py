from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts_create/', views.AccountCreateView.as_view(), name='create'),
]
