from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, FormView, ListView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm


# Create your views here.
def hello(request):
    # HttpResponse関数は引数の文字列をwebページに引き渡す
    return HttpResponse('<h1>Hello, myapp2!</h1>')


class StaffListView(ListView):
    model = Staff
    template_name = 'myapp2/staff_list.html'


class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'
    # 処理が成功した場合のリダイレクト先
    # 追加・削除・更新は処理の後にリダイレクトするのが普通
    # URLの逆引き app_name:path関数のname
    success_url = reverse_lazy('myapp:home')
    # 結果的に次のようになっている
    # success_url = '/home/'


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'myapp2/department_create.html'
    success_url = reverse_lazy('myapp:home')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp2/book_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    success_url = reverse_lazy('myapp:home')

# CreateViewの中で行われている処理の流れ

# def staff_information(request):
#     if request.method == 'POST':
#         form = StaffInformationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:home')
#         else:
#             context = {
#                 'form': form,
#             }
#             return render(request, 'myapp/staff_information_create.html', context)
#     else:
#         form = StaffInformationForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'myapp/staff_information_create.html', context)
