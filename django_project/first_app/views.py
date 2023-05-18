import random

from django.shortcuts import render


# Create your views here.

class Student:
    def __init__(self, _id, name, points):
        self.id = _id
        self.name = name
        self.points = points


def main_page(request):
    teacher = "Vladyslav"
    students = []
    for i in range(1, 11):
        s = Student(1, f"Student Name {i}", points=random.randint(60, 100))
        students.append(s)
    return render(request=request, template_name="base.html",
                  context={"teacher": teacher,
                           "students": students,
                           "group_id": 1,
                           })


def lessons_page(request):
    return render(request=request, template_name="lessons.html",
                  context={"teacher": "Vladyslav",
                           "group_id": 1,
                           })


def notes_page(request):
    return  render(request, "notes.html")

