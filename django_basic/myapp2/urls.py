
from django.urls import path
from . import views

app_name = 'myapp2'
urlpatterns = [
    path('staff_information_create/', views.StaffInformationCreateView.as_view(), name='staff_information_create'),
    path('department_create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('staff_create/', views.StaffCreateView.as_view(), name='staff_create'),
    path('staff_list/', views.StaffListView.as_view(), name='staff_list'),
    path('department_list/', views.DepartmentListView.as_view(), name='department_list'),
    # <データの型:変数名> int型の値が埋め込まれて、pkという名前でビューで使えます　という意味
    path('staff_detail/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),
    path('staff_information_update/<int:pk>/', views.StaffInformationUpdateView.as_view(),
         name='staff_information_update'),
    path('hello/', views.hello, name='hello')
]
