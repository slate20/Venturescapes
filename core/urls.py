from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("main_layout/", views.main_layout, name="main_layout"),
    path("biz_setup/", views.biz_setup, name="biz_setup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("opportunities/", views.opportunities, name="opportunities"),
    path("get_job_details/<int:job_id>/", views.get_job_details, name="get_job_details"),
    path("accept_job/<int:job_id>/", views.accept_job, name="accept_job"),
    path("decline_job/<int:job_id>/", views.decline_job, name="decline_job"),
]