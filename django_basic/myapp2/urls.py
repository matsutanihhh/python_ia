
from django.urls import path
from . import views

app_name = 'myapp2'
urlpatterns = [
    path('staff_information_create/', views.StaffInformationCreateView.as_view(), name='staff_information_create'),
    path('department_create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('staff_create/', views.StaffCreateView.as_view(), name='staff_create'),
    path('staff_list/', views.StaffListView.as_view(), name='staff_list'),
    path('hello/', views.hello, name='hello')
]
