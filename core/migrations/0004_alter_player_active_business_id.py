# Generated by Django 5.1.2 on 2024-10-20 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_player_player_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='active_business_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.business'),
        ),
    ]
