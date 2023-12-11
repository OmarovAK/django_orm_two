from django.contrib import admin

from model_migrate.models import Teacher, Student, Teacher_Student


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']


class InlineTeacherStudent(admin.TabularInline):
    model = Teacher_Student
    fields = ['teacher']


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    inlines = [InlineTeacherStudent, ]
    list_display = ['id', 'name', 'group']
