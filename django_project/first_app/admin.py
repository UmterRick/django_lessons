from django.contrib import admin
from .models import Group, Lesson, StudentLessonRelation, LMSUser


# Register your models here.

@admin.register(LMSUser)
class LmsUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentLessonRelation)
class StudentLessonAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Student, StudentsAdmin)
