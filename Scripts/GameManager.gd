extends Node

#Preload Data.gd
const Data = preload("res://Scripts/Data.gd")

# Global Game State
var company = Data.Company
var funds = 10000
var rank = 1.0
var reputation = 50


var opportunities: Array[Data.RequestOpportunity] = []
var active_service_jobs: Array[Data.ServiceJob] = []
var completed_service_jobs: Array[Data.ServiceJob] = []
var weekly_reports: Array[Data.WeeklyReport] = []

func _ready():
	print("Game Manager Ready")

func initialize_company(company_name: String, business_type: String):
	company = Data.Company.new()
	company.name = company_name
	company.business_type = business_type
	company.funds = funds
	company.rank = rank
	company.reputation = reputation
	print("Company initialized: ", company.name, " - ", company.business_type)

func adjust_funds(amount):
	funds += amount
	if company:
		company.funds = funds
	print("Funds adjusted by %d, new balance: %d" % [amount, funds])

func adjust_rank(amount):
	rank += amount
	if company:
		company.rank = rank
	print("Rank adjusted by %d, new rank: %d" % [amount, rank])

func adjust_reputation(amount):
	reputation += amount
	if company:
		company.reputation = reputation
	print("Reputation adjusted by %d, new reputation: %d" % [amount, reputation])
