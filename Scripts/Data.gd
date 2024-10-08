class_name GameData

class Player:
	var player_id: int
	var player_name: String
	var current_funds: int
	var active_business_id: int # Foreign Key to Business
	var experience_level: int
	var total_businesses_owned: int
		
class Competitor:
	var ai_id: int
	var financial_health: String
	var growth_level: int
	var perceived_strategy: String
	var failure_rate: float
	var failed_jobs: int
	var business_status: String # Active, Struggling, Bankrupt

class Business:
	var business_id: int
	var player_id: int # Foreign Key to Player
	var ai_id: int # Foreign Key to AI
	var business_name: String
	var business_type: String
	var industry: String
	var rank: float
	var reputation: int
	var weekly_revenue: int
	var weekly_expenses: int
	var weekly_profit: int
	var net_worth: int
	var financial_health: String
	var business_status: String
	var date_founded: String
	var growth_level: int
	var failure_rate: float
	var missed_deadlines: int

class Job:
	var job_id: int
	var business_id: int # Foreign Key to Business
	var job_name: String
	var job_type: String
	var client_name: String
	var deadline: int
	var payout: int
	var status: String
	var penalty: int 
	var job_status: String # Pending, In Progress, Completed, Late
	
class CustomerOrder:
	var order_id: int
	var reseller_id: int # Foreign Key to Reseller
	var client: String
	var products: Array[ProductOrder]
	var destination: String
	var deadline: int
	var payout: int
	var status: String
	var penalty: int

class PurchaseOrder:
	var purchase_order_id: int
	var reseller_id: int # Foreign Key to Reseller who is the customer
	var manufacturer_id: int # Foreign Key to Manufacturer
	var products: Array[ProductOrder] # Array of ProductOrder objects
	var destination: String
	var deadline: int
	var status: String
	var penalty: int

class ProductOrder:
	var product_id: int # Foreign Key to Product
	var quantity: int

class Contract:
	var contract_id: int
	var business_id: int # Foreign Key to Business
	var contract_type: String # Service, Product
	var start_date: String
	var end_date: String
	var sla: int # amount of client jobs that can be missed or ignored, or deliveries that can be late before penalty is applied
	var sla_violations: int # amount of times the SLA has been violated
	var product_id: Array[ProductOrder] # for product contracts
	var recurring_payment: int # amount of money paid per month (4 weeks)
	var delivery_schedule: int # amount of weeks between deliveries
	var status: String

class Asset:
	var asset_id: int
	var business_id: int # Foreign Key to Business
	var asset_name: String
	var asset_type: String # Real Estate, Equipment, Vehicle
	var asset_subtype: String # Warehouse, Office, Delivery Vehicle, etc.
	var purchase_price: int
	var purchase_date: String
	var condition: float # for non real estate assets, affects productivity
	var maintenance_cost: int
	var deterioration_rate: float # rate that assets condition decreases over time
	var upgrade_status: String
	var inventory: Array[StoredProduct] # only for subtypes with storage ability
	var capacity: int # max inventory level for subtypes with storage ability

class StoredProduct:
	var product_id: int # Foreign Key to Product
	var quantity: int

class RnDProject:
	var project_id: int
	var business_id: int # Foreign Key to Business
	var project_name: String
	var project_type: String
	var duration: int # in weeks
	var cost: int
	var progress: float
	var status: String
	var reward: String 

class Market:
	var market_id: int
	var industry: String
	var demand_level: float
	var saturation_level: float
	var growth_rate: float
	var seasonal_influence: float

class Product:
	var product_id: int
	var product_name: String
	var market_id: int # Foreign Key to Market
	var base_value: int
	var supply: int
	var demand: int
	var production_cost: int # cost per production cycle
	var production_time: int # time it takes for a production cycle
	var production_rate: int # amount of units produced per cycle
	var storage_size: int # how much inventory space a unit takes up


class WeeklyReport:
	var week: int
	var revenue: int
	var expenses: int
	var net_profit: int
	var rank_change: float
	var reputation_change: int

class RequestOpportunity:
	var id: String
	var title: String
	var description: String
	var client: String
	var time_estimate: int
	var payout: int
	var deadline: int


class BidOpportunity:
	var id: String
	var title: String
	var description: String
	var client: String
	var time_estimate: int
	var payout: int
	var deadline: int

class ServiceJob:
	var id: String
	var opportunity: RequestOpportunity
	var progress: float
	var time_spent: int
	var start_week: int
