from django.shortcuts import render, HttpResponse
from .models import Lesson, StudentLessonRelation, Group, LMSUser


# Create your views here.


def main_page(request):
    group = Group.objects.first()
    teacher = LMSUser.objects.get(group=group, role='teacher')
    relations = StudentLessonRelation.objects.filter(student__group=group.pk)
    lessons = Lesson.objects.all()
    journal = {}
    for relation in relations:

        if relation.student not in journal:
            journal[relation.student] = [relation]
        else:
            journal[relation.student].append(relation)

    return render(request=request, template_name="journal.html",
                  context={"teacher": teacher,
                           "journal": journal,
                           "lessons": lessons,
                           "rels": relations,
                           "group": group,
                           })


def render_lesson_info(request):
    ...


def render_student_profile(request, pk):
    student = LMSUser.objects.get(pk=pk)

    return HttpResponse(student)
