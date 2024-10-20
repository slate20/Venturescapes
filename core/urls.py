from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("main_layout/", views.main_layout, name="main_layout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("player_setup/", views.player_setup, name="player_setup"),
]