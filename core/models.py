from django.db import models

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    current_funds = models.IntegerField()
    active_business_id = models.ForeignKey('Business', on_delete=models.CASCADE, null=True, blank=True)
    experience_level = models.IntegerField()
    total_businesses_owned = models.IntegerField()

class Competitor(models.Model):
    ai_id = models.AutoField(primary_key=True)
    financial_health = models.CharField(max_length=50)
    growth_level = models.IntegerField()
    perceived_strategy = models.CharField(max_length=100)
    failure_rate = models.FloatField()
    business_status = models.CharField(max_length=50)

class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    player_owwner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    ai_owner = models.ForeignKey(Competitor, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    rank = models.FloatField()
    reputation = models.IntegerField()
    weekly_revenue = models.IntegerField()
    weekly_expenses = models.IntegerField()
    weekly_profit = models.IntegerField()
    net_worth = models.IntegerField()
    financial_health = models.CharField(max_length=50)
    business_status = models.CharField(max_length=50)
    date_founded = models.CharField(max_length=50)
    growth_level = models.IntegerField()
    failure_rate = models.FloatField()
    missed_deadlines = models.IntegerField()

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    job_name = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)  # Direct or Marketplace Bid
    client_name = models.CharField(max_length=255)
    expiration = models.IntegerField()
    deadline = models.IntegerField()
    payout = models.IntegerField()
    status = models.CharField(max_length=255)  # Pending, In Progress, Completed, Late
    penalty = models.IntegerField()  # amount of money deducted per week from payout if late

class CustomerOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    reseller_id = models.IntegerField() # foreign key to reseller
    client = models.CharField(max_length=255)
    products = models.ManyToManyField('ProductOrder')
    destination = models.CharField(max_length=255)
    deadline = models.IntegerField()
    payout = models.IntegerField()
    status = models.CharField(max_length=255)
    penalty = models.IntegerField()

class PurchaseOrder(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    reseller_id = models.IntegerField() # foreign key to reseller
    manufacturer_id = models.IntegerField() # foreign key to manufacturer
    products = models.ManyToManyField('ProductOrder')
    destination = models.CharField(max_length=255)
    deadline = models.IntegerField()
    status = models.CharField(max_length=255)
    penalty = models.IntegerField()

class ProductOrder(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    contract_type = models.CharField(max_length=255)  # Service, Product
    start_date = models.DateField()
    end_date = models.DateField()
    sla = models.IntegerField()  # amount of client jobs that can be missed or ignored, or deliveries that can be late before penalty is applied
    sla_violations = models.IntegerField()  # amount of times the SLA has been violated
    product_id = models.ManyToManyField('ProductOrder')  # for product contracts
    recurring_payment = models.IntegerField()  # amount of money paid per month (4 weeks)
    delivery_schedule = models.IntegerField()  # amount of weeks between deliveries
    status = models.CharField(max_length=255)

class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)  # Real Estate, Equipment, Vehicle
    asset_subtype = models.CharField(max_length=255)  # Warehouse, Office, Delivery Vehicle, etc.
    purchase_price = models.IntegerField()
    purchase_date = models.DateField()
    location = models.CharField(max_length=255, null=True, blank=True)
    condition = models.FloatField()  # for non real estate assets, affects productivity
    maintenance_cost = models.IntegerField()
    deterioration_rate = models.FloatField()  # rate that assets condition decreases over time
    upgrade_status = models.CharField(max_length=255)
    inventory = models.ManyToManyField('StoredProduct')  # only for subtypes with storage ability
    capacity = models.IntegerField()  # max inventory level for subtypes with storage ability

class StoredProduct(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class RnDProject(models.Model):
    project_id = models.AutoField(primary_key=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in weeks
    cost = models.IntegerField()
    progress = models.FloatField()
    status = models.CharField(max_length=255)
    reward = models.CharField(max_length=255)

class Market(models.Model):
    market_id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=255)
    demand_level = models.FloatField()
    saturation_level = models.FloatField()
    growth_rate = models.FloatField()
    seasonal_influence = models.FloatField()

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    market_id = models.ForeignKey('Market', on_delete=models.CASCADE)
    base_value = models.IntegerField()
    supply = models.IntegerField()
    demand = models.IntegerField()
    production_cost = models.IntegerField()  # cost per production cycle
    production_time = models.IntegerField()  # time it takes for a production cycle
    production_rate = models.IntegerField()  # amount of units produced per cycle
    storage_size = models.IntegerField()  # how much inventory space a unit takes up

class WeeklyReport(models.Model):
    week = models.IntegerField()
    revenue = models.IntegerField()
    expenses = models.IntegerField()
    profit = models.IntegerField()