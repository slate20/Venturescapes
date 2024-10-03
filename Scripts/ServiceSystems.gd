extends Node

# Load Data
const Data = preload("res://Scripts/Data.gd")

var company: Data.Company
var opportunities: Array[Data.RequestOpportunity]
var active_service_jobs: Array[Data.ServiceJob]
var completed_service_jobs: Array[Data.ServiceJob]
var weekly_reports: Array[Data.WeeklyReport]

func _ready():
	initialize_game()
	
func initialize_game():
	company = Data.Company.new()
	company.name = "Acme Corporation"
	company.funds = 10000
	company.rank = 1.0
	company.reputation = 50

	generate_opportunities(5)

func generate_opportunities(count: int):
	for i in range(count):
		var opp = Data.RequestOpportunity.new()
		opp.id = "OPP" + str(opportunities.size() + 1)
		opp.title = "Project " + str(opportunities.size() + 1)
		opp.description = "This is a sample project"
		opp.client = "Client " + str(randi() % 10 + 1)
		opp.time_estimate = randi() % 14 + 7 # 1-3 weeks
		opp.payout = (opp.time_estimate * 100)
		opp.deadline = randi() % 4 + 2 # 2-5 weeks
		opportunities.append(opp)

func accept_opportunity(opp_id: String):
	var opp = opportunities.filter(func(o): return o.id == opp_id)[0]
	var service_job = Data.ServiceJob.new()
	
	service_job.id = "JOB" + str(active_service_jobs.size() + 1)
	service_job.opportunity = opp
	service_job.progress = 0.0
	service_job.time_spent = 0
	service_job.start_week = TurnManager.current_week
	
	active_service_jobs.append(service_job)
	opportunities.erase(opp)

func work_on_job(job_id: String, days: int):
	var job = active_service_jobs.filter(func(j): return j.id == job_id)[0]
	
	job.progress += days / job.opportunity.estimated_time
	job.time_spent += days
	
	TurnManager.days_left -= days

func submit_job(job_id: String):
	var job = active_service_jobs.filter(func(j): return j.id == job_id)[0]
	
	active_service_jobs.erase(job)
	completed_service_jobs.append(job)
	
	# Calculate payout
	var payout = job.opportunity.payout
	var weeks_over = max(0, ceil(float(job.time_spent - job.opportunity.estimated_time) / 7))
	
	if weeks_over > 0:
		var deduction_percentage = weeks_over * 0.1
		payout = max(0, payout * (1 - deduction_percentage))
	
	TurnManager.weekly_revenue += payout
