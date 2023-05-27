from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import Lesson, StudentLessonRelation, Group, LMSUser


# Create your views here.


def main_page(request):
    group = Group.objects.first()
    teacher = LMSUser.objects.get(group=group, role='teacher')
    students = LMSUser.objects.filter(group=group, role='student')
    relations = StudentLessonRelation.objects.filter(student__group=group.pk).order_by('lesson__date')
    lessons = Lesson.objects.all().order_by('date')
    journal = {}
    for relation in relations:
        if relation.student.pk not in journal:
            journal[relation.student.pk] = {relation.lesson.pk: relation}
        else:
            journal[relation.student.pk].update({relation.lesson.pk: relation})
    return render(request=request, template_name="journal.html",
                  context={"teacher": teacher,
                           "journal": journal,
                           "lessons": lessons,
                           "students": students,
                           "group": group,
                           })


def render_lesson_info(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    return render(request=request, template_name="lesson.html", context={"lesson": lesson})


def render_student_profile(request, pk):
    student = LMSUser.objects.get(pk=pk)

    return render(request=request, template_name="student.html", context={"user": student})


def switch_student_visited(request, student_pk, lesson_pk):
    relation = StudentLessonRelation.objects.get(student_id=student_pk, lesson_id=lesson_pk)
    relation.change_visited()
    return redirect(main_page)


def render_lessons_list(request):
    active_lesson_id = request.GET.get("active_lesson_id", None)
    lessons = Lesson.objects.all().order_by("date")

    if not lessons:
        return HttpResponseNotFound("Lessons are not found")
    if active_lesson_id:
        active_lesson = Lesson.objects.get(title=active_lesson_id)
    else:
        active_lesson = lessons.first()
    return render(request, "lessons_list.html", context={"lessons": lessons,
                                                         "active_lesson": active_lesson})
