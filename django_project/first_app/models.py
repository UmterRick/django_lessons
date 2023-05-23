from django.db import models
from django.contrib.auth.models import User
import uuid


class Teacher(User):
    is_staff = True


class Group(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()


class Student(User):
    is_staff = False
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    date = models.DateField()


class StudentLessonRelation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    comment = models.TextField()
    points = models.IntegerField(default=0)
