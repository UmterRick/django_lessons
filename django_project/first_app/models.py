from django.db import models
from django.contrib.auth.models import User
import uuid


class Group(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()


class LMSUser(User):
    role = models.CharField(max_length=30, null=False, choices=[("student", "Student"), ("teacher", "Teacher")])
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, default=None)


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    date = models.DateField()


class StudentLessonRelation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    comment = models.TextField()
    points = models.IntegerField(default=0)
