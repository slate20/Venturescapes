# Generated by Django 5.1.2 on 2024-10-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_job_expiration'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='completion_time',
            field=models.IntegerField(default=3),
        ),
    ]
