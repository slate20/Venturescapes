from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("main_layout/", views.main_layout, name="main_layout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("opportunities/", views.opportunities, name="opportunities"),
    path("biz_setup/", views.biz_setup, name="biz_setup"),
]