from core.models import Business, Job
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