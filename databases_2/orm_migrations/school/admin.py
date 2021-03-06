from django.contrib import admin

from .models import Student, Teacher, StudentTeachers

class ChoiceInlane(admin.TabularInline):
    model = StudentTeachers

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlane]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlane]
