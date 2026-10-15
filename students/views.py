from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Student, ClassInfo


# ==================== 首页 ====================
def index(request):
    """首页：展示网站名称、导航菜单（Bootstrap样式）"""
    student_count = Student.objects.count()
    class_count = ClassInfo.objects.count()
    context = {
        'student_count': student_count,
        'class_count': class_count,
    }
    return render(request, 'students/index.html', context)


# ==================== 学生列表页 ====================
class StudentListView(ListView):
    """学生列表页：展示所有学生信息（表格形式）"""
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10  # 分页


# ==================== 学生详情页 ====================
class StudentDetailView(DetailView):
    """学生详情页：查看单个学生详细信息"""
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'pk'


# ==================== 添加学生页 ====================
class StudentCreateView(CreateView):
    """添加学生页面：表单提交并保存到数据库"""
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'gender', 'age', 'class_name', 'student_id']
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '添加学生'
        return context

    def form_valid(self, form):
        messages.success(self.request, '学生添加成功！')
        return super().form_valid(form)


# ==================== 编辑学生页 ====================
class StudentUpdateView(UpdateView):
    """编辑学生页面"""
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'gender', 'age', 'class_name', 'student_id']
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '编辑学生'
        return context

    def form_valid(self, form):
        messages.success(self.request, '学生信息修改成功！')
        return super().form_valid(form)


# ==================== 删除学生 ====================
class StudentDeleteView(DeleteView):
    """删除学生页面"""
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    context_object_name = 'student'

    def delete(self, request, *args, **kwargs):
        messages.success(request, '学生删除成功！')
        return super().delete(request, *args, **kwargs)
