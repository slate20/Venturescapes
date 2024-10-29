from django.core.management.base import BaseCommand
from core.models import GameState

class Command(BaseCommand):
    help = 'Initialize the gamestate if it does not exist'

    def handle(self, *args, **options):
        state, created = GameState.objects.get_or_create(pk=1)
        if created:
            self.stdout.write(self.style.SUCCESS('Gamestate initialized successfully.'))
        else:
            self.stdout.write(self.style.ERROR('Gamestate already exists.'))