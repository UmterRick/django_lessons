from django.shortcuts import render, HttpResponse, redirect
from .models import Lesson, StudentLessonRelation, Group, LMSUser


# Create your views here.


def main_page(request):
    group = Group.objects.first()
    teacher = LMSUser.objects.get(group=group, role='teacher')
    relations = StudentLessonRelation.objects.filter(student__group=group.pk).order_by('lesson__date')
    lessons = Lesson.objects.all().order_by('date')
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

    return render(request=request, template_name="student.html", context={"user": student})


def switch_student_visited(request, student_pk, lesson_pk):
    relation = StudentLessonRelation.objects.get(student_id=student_pk, lesson_id=lesson_pk)
    relation.visited = not relation.visited
    relation.save()
    return redirect(main_page)
