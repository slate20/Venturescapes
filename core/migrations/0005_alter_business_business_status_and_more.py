# Generated by Django 5.1.2 on 2024-10-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_player_active_business_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_status',
            field=models.CharField(default='Active', max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='date_founded',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='failure_rate',
            field=models.FloatField(default=0.1),
        ),
        migrations.AlterField(
            model_name='business',
            name='financial_health',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='growth_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='missed_deadlines',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='net_worth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='rank',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='business',
            name='reputation',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='business',
            name='weekly_expenses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='weekly_profit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='weekly_revenue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='Direct', max_length=255),
        ),
    ]
