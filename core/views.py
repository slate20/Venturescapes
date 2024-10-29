from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.dateformat import DateFormat
from core.services.auth_service import AuthService
from core.services.business_service import BusinessService
from core.services.job_service import JobService
from .models import Player, Business, Job, GameState


# Create your views here.
def register(request):
    return AuthService.register(request)

def login_view(request):
    return AuthService.login_user(request)

def logout_view(request):
    return AuthService.logout_user(request)

@login_required
def main_layout(request):
    current_time = timezone.now()
    formatted_time = DateFormat(current_time).format('g:i A')
    jobs = Job.objects.filter(business_id=request.user.player.active_business_id)
    context = {
        'server_time': formatted_time,
        'game_day': GameState.objects.first().current_day,
        'game_week': GameState.objects.first().current_week,
        'game_year': GameState.objects.first().current_year,
    }
    return render(request, 'main_layout.html', context=context)

@login_required
def dashboard(request):
    # Get the current business
    current_business = request.user.player.active_business_id

    # Fetch the jobs for the current business
    jobs = Job.objects.filter(
        business_id=current_business,
        status='In Progress'
    )

    for job in jobs:
        job_progress = round(job.time_worked / job.completion_time * 100) if job.completion_time != 0 else 0

    context = {
        'jobs': jobs,
        'hx_view': 'true',
        'job_progress': job_progress,
    }

    return render(request, 'dashboard.html', context)

def biz_setup(request):
    return BusinessService.new_business_setup(request)
        
@login_required
def opportunities(request):
    # Get the current business
    current_business = request.user.player.active_business_id

    # Fetch the direct request jobs for the current business
    direct_requests = Job.objects.filter(
        business_id=current_business,
        job_type='Direct',
        status='Pending'
    )

    context = {
        'direct_requests': direct_requests,
        'hx_view': 'true'
    }

    return render(request, 'opportunities.html', context)

@login_required
def get_job_details(request, job_id):
    job = Job.objects.get(job_id=job_id)

    return JobService.get_job_details(request, job)

@login_required
def accept_job(request, job_id):
    job = Job.objects.get(job_id=job_id)

    JobService.accept_job(job)

    return opportunities(request)

@login_required
def decline_job(request, job_id):
    job = Job.objects.get(job_id=job_id)
    
    JobService.decline_job(job)

    return opportunities(request)

@login_required
def pipeline(request):
    return render(request, 'pipeline_items.html')

@login_required
def work_on_job(request, job_id):
    job = Job.objects.get(job_id=job_id)

    JobService.work_on_job(job)

    return render(request, 'main_layout.html', {'job': job})