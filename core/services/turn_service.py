from core.models import GameState, Player, Job, Business
from core.services.job_service import JobService

class TurnService:

    @staticmethod
    def advance_day():
        # Increment the day
        state = GameState.objects.first()
        state.current_day += 1
        state.save()

        # Process jobs for all players
        players_working = Player.objects.filter(working_job__isnull=False)

        for player in players_working:
            job = player.working_job
            job.time_worked += 1
            job.progress = round(job.time_worked / job.completion_time * 100)
            job.save()

            # Check if the job is completed
            if job.time_worked >= job.completion_time:
                job.status = 'Completed'
                job.save()

                # Remove from working jobs
                player.current_task = None
                player.working_job = None
                player.save()

        # Print success message to console
        print('Advanced to day ' + str(state.current_day))

    
    @staticmethod
    def advance_week():
        state = GameState.objects.first()
        # process day 7
        if state.current_day == 7:
            TurnService.advance_day()

        # Increment the week and set the day to 1

        if state.current_week == 52:
            state.current_day = 1
            state.current_week = 1
            state.current_year += 1
            state.save()
        else:
            state.current_week += 1
            state.current_day = 1
            state.save()

        # Process weekly profit for all businesses
        businesses = Business.objects.all()
        for business in businesses:
            business.weekly_profit = business.weekly_revenue - business.weekly_expenses

            # Add profit to player's balance
            player = business.player_owner
            player.current_funds += business.weekly_profit
            player.save()

            # Reset weekly revenue and expenses
            business.weekly_revenue = 0
            business.weekly_expenses = 0
            business.weekly_profit = 0
            business.save()

            # Generate new jobs for business
            JobService.generate_direct_requests(business, 3)

        # Print success message to console
        print('Advanced to week ' + str(state.current_week) + ' of year ' + str(state.current_year))

