from django.contrib import admin

from .models import Department, Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ("name", "age", "course", "phone")
	search_fields = ("name", "course")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	search_fields = ("name",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ("name", "department")
	list_filter = ("department",)
	search_fields = ("name",)
