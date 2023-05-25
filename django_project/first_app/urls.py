from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.main_page, name="journal-url"),
    path('lesson/<uuid:pk>', views.render_lesson_info, name="lesson-info"),
    path('student/<int:pk>', views.render_student_profile, name="student-info"),
    path('student/<int:student_pk>/lesson/<uuid:lesson_pk>/change-visited', views.switch_student_visited, name="switch-visited")

]
