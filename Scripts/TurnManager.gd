extends Node

const Data = preload("res://Scripts/Data.gd")

var days_left = 7
var current_week = 1
var current_year = 2024
var weekly_revenue = 0
var weekly_expense = 0
var weekly_profit = 0

func _ready():
	print("TurnManager Ready")

func advance_week():
	# Update date
	current_week += 1
	days_left = 7
	if current_week > 52:
		current_week = 1
		current_year += 1

	print("Advancing to week %d of %d" % [current_week, current_year])
	
	# Process weekly profit
	weekly_profit = weekly_revenue - weekly_expense
	
	# Generate new opportunities
	ServiceSystems.generate_opportunities(randi() % 3 + 1) # 1-3 new opportunities per week
	
	# Create weekly report
	var report = Data.WeeklyReport.new()
	
	report.week = current_week
	report.revenue = weekly_revenue
	report.expenses = weekly_expense
	report.net_profit = weekly_profit
	report.rank_change = 0
	report.reputation_change = 0
	
	GameManager.weekly_reports.append(report)
	
	# Reset completed projects
	ServiceSystems.completed_service_jobs.clear()

	# Update the dashboard
	var main_layout = get_tree().get_root().get_node("GameUI/MainLayout")
	var dashboard = main_layout.get_node("MainContent/Dashboard")
	if dashboard:
		dashboard.update_dashboard()
	else:
		print("Dashboard not found")

func get_current_state():
	return {
		"company": GameManager.company,
		"opportunities": ServiceSystems.opportunities,
		"active_jobs": ServiceSystems.active_service_jobs,
		"completed_jobs": ServiceSystems.completed_service_jobs,
		"weekly_report": GameManager.weekly_reports[-1] if GameManager.weekly_reports else null
	}
