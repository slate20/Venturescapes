from django.core.management.base import BaseCommand
from core.services.turn_service import TurnService

class Command(BaseCommand):
    help = 'Advance the game to the next turn'

    def handle(self, *args, **options):
        TurnService.advance_week()