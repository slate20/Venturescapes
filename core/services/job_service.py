from urllib import request
from core.models import Business, Job, GameState, Player
from django.shortcuts import render
import random


class JobService:

    @staticmethod
    def generate_direct_requests(business, num_jobs=3):
        job_names = ["Create Landing Page", "Build Website", "Build Mobile App"]
        client_names = ["Client A", "Client B", "Client C"]
        payouts = [1000, 800, 1500]
        durations = [3, 5, 7] #number of days until completion
        deadlines = [2, 3, 5] #number of weeks/turns until due

        for _ in range(num_jobs):
            Job.objects.create(
                business_id=business,
                job_name=random.choice(job_names),
                client_name=random.choice(client_names),
                completion_time=random.choice(durations),
                deadline=random.choice(deadlines),
                payout=random.choice(payouts),
                status="Pending",
                penalty=500 # Flat penalty for late jobs
            )

    @staticmethod
    def get_job_details(request, job):

        week_deadline = GameState.get_current().current_week + job.deadline
        if week_deadline > 52:
            year_deadline = GameState.get_current().current_year + 1
        else:
            year_deadline = GameState.get_current().current_year
        job_deadline = "Week " + str(week_deadline) + ", " + str(year_deadline)

        content = {
            'job': job,
            'job_deadline': job_deadline
        }

        if job.job_type == 'Direct':
            return render(request, 'direct_job_details.html', content)

        else:
            return render(request, 'marketplace_job_details.html', content)
        
    @staticmethod
    def accept_job(job):
        job.status = 'In Progress'
        job.save()

    @staticmethod
    def decline_job(job):
        job.status = 'Declined'
        job.save()

    @staticmethod
    def work_on_job(job):
        player = Player.objects.get(user=request.user)

        player.current_task = job.job_name
        player.working_job = job