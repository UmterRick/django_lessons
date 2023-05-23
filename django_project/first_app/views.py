from django.shortcuts import render
from .models import Lesson, StudentLessonRelation

# Create your views here.




def main_page(request):
    teacher = ...
    students = []
    return render(request=request, template_name="base.html",
                  context={"teacher": teacher,
                           "students": students,
                           "group_id": 1,
                           })


def render_lesson_info(request):
    ...

def render_student_profile(request):
    ...




