from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("main_layout/", views.main_layout, name="main_layout"),
    path("top_bar/", views.top_bar, name="top_bar"),
    path("biz_setup/", views.biz_setup, name="biz_setup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("opportunities/", views.opportunities, name="opportunities"),
    path("get_job_details/<int:job_id>/", views.get_job_details, name="get_job_details"),
    path("accept_job/<int:job_id>/", views.accept_job, name="accept_job"),
    path("decline_job/<int:job_id>/", views.decline_job, name="decline_job"),
    path("pipeline/", views.pipeline, name="pipeline"),
    path("work_on_job/<int:job_id>/", views.work_on_job, name="work_on_job"),
    path("stop_working_job/<int:job_id>/", views.stop_working_job, name="stop_working_job"),
    path("complete_job/<int:job_id>/", views.complete_job, name="complete_job"),
]