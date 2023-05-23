from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.main_page),
    path('lesson/<UUID:pk>', views.render_lesson_info, name="lesson-info"),
    path('student/<UUID:pk>', views.render_student_profile, name="student-info"),

]
