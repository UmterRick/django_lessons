from django.db import models
from django.contrib.auth.models import User
import uuid


class Group(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class LMSUser(User):
    role = models.CharField(max_length=30, null=False, choices=[("student", "Student"), ("teacher", "Teacher")])
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.email

class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class StudentLessonRelation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    comment = models.TextField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student} - {self.lesson} {'Visited' if self.visited else 'Missed'}"
