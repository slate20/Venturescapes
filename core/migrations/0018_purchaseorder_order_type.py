# Generated by Django 5.1.2 on 2024-10-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_job_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='order_type',
            field=models.CharField(default='Direct', max_length=255),
        ),
    ]
