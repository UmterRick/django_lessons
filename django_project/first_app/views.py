import random

from django.shortcuts import render
from .models import Lesson, Student, StudentLessonRelation

# Create your views here.




def main_page(request):
    teacher = "Vladyslav"
    students = []
    return render(request=request, template_name="base.html",
                  context={"teacher": teacher,
                           "students": students,
                           "group_id": 1,
                           })




