from django.db import models
from django.contrib.auth.models import User
import uuid


class Student(User):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_staff = False


class Teacher(User):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_staff = True


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()


class StudentLessonRelation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    comment = models.TextField()
    points = models.IntegerField(default=0)
