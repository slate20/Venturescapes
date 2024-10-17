# Generated by Django 5.1.2 on 2024-10-17 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('ai_id', models.AutoField(primary_key=True, serialize=False)),
                ('financial_health', models.CharField(max_length=50)),
                ('growth_level', models.IntegerField()),
                ('perceived_strategy', models.CharField(max_length=100)),
                ('failure_rate', models.FloatField()),
                ('business_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('market_id', models.AutoField(primary_key=True, serialize=False)),
                ('industry', models.CharField(max_length=255)),
                ('demand_level', models.FloatField()),
                ('saturation_level', models.FloatField()),
                ('growth_rate', models.FloatField()),
                ('seasonal_influence', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('revenue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('business_name', models.CharField(max_length=100)),
                ('business_type', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('rank', models.FloatField()),
                ('reputation', models.IntegerField()),
                ('weekly_revenue', models.IntegerField()),
                ('weekly_expenses', models.IntegerField()),
                ('weekly_profit', models.IntegerField()),
                ('net_worth', models.IntegerField()),
                ('financial_health', models.CharField(max_length=50)),
                ('business_status', models.CharField(max_length=50)),
                ('date_founded', models.CharField(max_length=50)),
                ('growth_level', models.IntegerField()),
                ('failure_rate', models.FloatField()),
                ('missed_deadlines', models.IntegerField()),
                ('ai_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.competitor')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=255)),
                ('job_type', models.CharField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
                ('expiration', models.IntegerField()),
                ('deadline', models.IntegerField()),
                ('payout', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('penalty', models.IntegerField()),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=100)),
                ('current_funds', models.IntegerField()),
                ('experience_level', models.IntegerField()),
                ('total_businesses_owned', models.IntegerField()),
                ('active_business_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.business')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='player_owwner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.player'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('base_value', models.IntegerField()),
                ('supply', models.IntegerField()),
                ('demand', models.IntegerField()),
                ('production_cost', models.IntegerField()),
                ('production_time', models.IntegerField()),
                ('production_rate', models.IntegerField()),
                ('storage_size', models.IntegerField()),
                ('market_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.market')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('reseller_id', models.IntegerField()),
                ('client', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('deadline', models.IntegerField()),
                ('payout', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('penalty', models.IntegerField()),
                ('products', models.ManyToManyField(to='core.productorder')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.AutoField(primary_key=True, serialize=False)),
                ('contract_type', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('sla', models.IntegerField()),
                ('sla_violations', models.IntegerField()),
                ('recurring_payment', models.IntegerField()),
                ('delivery_schedule', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
                ('product_id', models.ManyToManyField(to='core.productorder')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('purchase_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('reseller_id', models.IntegerField()),
                ('manufacturer_id', models.IntegerField()),
                ('destination', models.CharField(max_length=255)),
                ('deadline', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('penalty', models.IntegerField()),
                ('products', models.ManyToManyField(to='core.productorder')),
            ],
        ),
        migrations.CreateModel(
            name='RnDProject',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
                ('project_type', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('progress', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('reward', models.CharField(max_length=255)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
            ],
        ),
        migrations.CreateModel(
            name='StoredProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_name', models.CharField(max_length=255)),
                ('asset_type', models.CharField(max_length=255)),
                ('asset_subtype', models.CharField(max_length=255)),
                ('purchase_price', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('condition', models.FloatField()),
                ('maintenance_cost', models.IntegerField()),
                ('deterioration_rate', models.FloatField()),
                ('upgrade_status', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
                ('inventory', models.ManyToManyField(to='core.storedproduct')),
            ],
        ),
    ]