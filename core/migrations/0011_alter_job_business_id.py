# Generated by Django 5.1.2 on 2024-10-28 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_job_completion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='business_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.business'),
        ),
    ]
