from django.urls import path
from auth_app import views

urlpatterns = [
    path("login", views.login_view, name="login_url"),
    path("logout", views.logout_view, name="logout_url"),
    path("register", views.register_view, name="register_url"),
]
