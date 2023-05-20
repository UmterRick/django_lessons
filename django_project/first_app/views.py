import random

from django.shortcuts import render
from .models import Book, Author

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
    books_to_render = Book.objects.all()
    return render(request=request, template_name="lessons.html",
                  context={"teacher": "Vladyslav",
                           "group_id": 1,
                           })


def library(request):
    p = Book.objects.all().order_by('rating').values('title', 'rating')
    print(p)
    p.title = "ahahahah prank"
    p.title = "sadasdnas"
    p.rating = 5

    p.save()


    return render(request=request, template_name="books.html",
                  context={"teacher": "Vladyslav",
                           "group_id": 1,
                           "books": Book.objects.all()
                           })

def notes_page(request):
    return  render(request, "notes.html")

