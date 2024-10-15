extends Node

#Preload Data.gd
const Data = preload("res://Scripts/Data.gd")

# Global Game State
var player: Data.Player
var businesses: Array[Data.Business] = []
var competitors: Array[Data.Competitor] = []
var opportunities: Array[Data.RequestOpportunity] = []
var active_service_jobs: Array[Data.ServiceJob] = []
var completed_service_jobs: Array[Data.ServiceJob] = []
var weekly_reports: Array[Data.WeeklyReport] = []

func _ready():
	print("Game Manager Ready")

func initialize_player(player_name: String):
	player = Data.Player.new()
	player.player_name = player_name
	player.current_funds = 10000
	player.experience_level = 5
	player.total_businesses_owned = 0
	player.player_id = 1
	player.active_business_id = 0
	print("Player initialized: ", player.player_name)

func create_business(business_name: String, business_type: String, industry: String):
	var new_business = Data.Business.new()
	new_business.business_id = businesses.size() + 1
	new_business.player_id = player.player_id
	new_business.business_name = business_name
	new_business.business_type = business_type
	new_business.industry = industry
	new_business.rank = 3.0
	new_business.reputation = 50
	new_business.growth_level = 1
	new_business.failure_rate = 0.1
	new_business.business_status = "Active"
	new_business.date_founded = TurnManager.current_date
	businesses.append(new_business)
	if player.active_business_id == 0:
		player.active_business_id = new_business.business_id
	player.total_businesses_owned += 1
	print("Business created: ", new_business.business_name, " - ", new_business.industry)
	return new_business

func get_active_business():
	for business in businesses:
		if business.business_id == player.active_business_id:
			return business
	return null

func switch_active_business(business_id: int):
	if business_id in businesses.map(func(b): return b.business_id):
		player.active_business_id = business_id
		print("Switched active business to: ", get_active_business().business_name)
	else:
		print("Business not found")

func adjust_funds(amount):
	player.current_funds += amount
	print("Funds adjusted by %d, new balance: %d" % [amount, player.current_funds])

func adjust_rank(amount):
	var active_business = get_active_business()
	active_business.rank += amount
	print("Rank adjusted by %d, new rank: %d" % [amount, active_business.rank])

func adjust_reputation(amount):
	var active_business = get_active_business()
	active_business.reputation += amount
	print("Reputation adjusted by %d, new reputation: %d" % [amount, active_business.reputation])

func get_player_business_location():
	var active_business = get_active_business()
	if active_business:
		return active_business.location
	return ""
