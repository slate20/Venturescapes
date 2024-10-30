from django.shortcuts import render, redirect
from core.models import Player, Business

class BusinessService:

    @staticmethod
    def new_business_setup(request):
        player = Player.objects.get(user=request.user)

        # If the player already has an active business, redirect to the main layout
        if player.active_business_id:
            return redirect('main_layout')
        else:
            if request.method == 'POST':
                business_name = request.POST.get('business_name')
                business_type = request.POST.get('business_type')
                industry = request.POST.get('industry')

                # Create a Business instance that belongs to the player
                business = Business.objects.create(
                    player_owner=player,
                    business_name=business_name,
                    business_type=business_type,
                    industry=industry
                )

                # Set the business as the player's active business
                player.active_business_id = business
                player.save()

                return redirect('main_layout')
            else:
                return render(request, 'player_setup.html')
            
    @staticmethod
    def get_job_details(request, job):
        if job.job_type == 'Direct':
            return render(request, 'direct_job_details.html', {'job': job})
        
        else:
            return render(request, 'marketplace_job_details.html', {'job': job})
        
    @staticmethod
    def accept_job(job):
        job.status = 'In Progress'
        job.save()

    @staticmethod
    def decline_job(job):
        job.status = 'Declined'
        job.save()