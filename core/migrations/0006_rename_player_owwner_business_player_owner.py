# Generated by Django 5.1.2 on 2024-10-20 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_business_business_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='player_owwner',
            new_name='player_owner',
        ),
    ]
