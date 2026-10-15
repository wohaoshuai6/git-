from django.db import models


class ClassInfo(models.Model):
    """班级模型"""
    name = models.CharField(max_length=50, verbose_name='班级名称', unique=True)

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = '班级信息'
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(models.Model):
    """学生模型"""
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )

    name = models.CharField(max_length=30, verbose_name='姓名')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='性别')
    age = models.PositiveSmallIntegerField(verbose_name='年龄')
    class_name = models.ForeignKey(
        ClassInfo,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='班级'
    )
    student_id = models.CharField(max_length=8, unique=True, verbose_name='学号', blank=True)

    def save(self, *args, **kwargs):
        """自动生成学号，从 10000001 开始递增"""
        if not self.student_id:
            last = Student.objects.order_by('-student_id').first()
            if last and last.student_id:
                self.student_id = str(int(last.student_id) + 1)
            else:
                self.student_id = '10000001'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
        ordering = ['class_name', 'name']

    def __str__(self):
        return f'{self.name} - {self.class_name.name}'
