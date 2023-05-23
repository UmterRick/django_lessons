from django.shortcuts import render
from .models import Lesson, StudentLessonRelation, Group, LMSUser


# Create your views here.


def main_page(request):
    group = Group.objects.first()
    teacher = LMSUser.objects.get(group=group, role='teacher')
    relations = StudentLessonRelation.objects.filter(student__group=group.pk)
    journal = []
    for relation in relations:
        journal.append({relation.student: relation})

    print(journal)

    return render(request=request, template_name="journal.html",
                  context={"teacher": teacher,
                           "journal": journal,
                           "group": group,
                           })


def render_lesson_info(request):
    ...


def render_student_profile(request):
    ...
