from django.urls import path
from . import views

urlpatterns = [
    # 首页
    path('', views.index, name='index'),

    # 学生列表页
    path('students/', views.StudentListView.as_view(), name='student_list'),

    # 学生详情页
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),

    # 添加学生
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),

    # 编辑学生
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),

    # 删除学生
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
