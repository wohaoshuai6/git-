from django.contrib import admin
from .models import Student, ClassInfo


@admin.register(ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'age', 'class_name', 'student_id')
    list_filter = ('gender', 'class_name')
    search_fields = ('name', 'student_id')
    list_per_page = 20
    list_editable = ('gender', 'age', 'class_name', 'student_id')
