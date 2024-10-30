from django.db import migrations
from django.core.management import call_command

def run_game_init(apps, schema_editor):
    call_command('game_init')

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(run_game_init),
    ]