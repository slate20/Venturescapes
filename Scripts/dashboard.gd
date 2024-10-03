extends Control

# Onready variables for UI elements
@onready var company_name_label = $CompanyInfo/CompanyName
@onready var business_type_label = $CompanyInfo/BusinessType
@onready var weekly_summary = $TabContainer/Overview/WeeklySummary
@onready var pipeline = $TabContainer/Overview/Pipeline/Container
@onready var news_alerts = $TabContainer/Overview/NewsAlerts/VBoxContainer
@onready var ytd_summary = $TabContainer/Overview/YTDSummary/VBoxContainer
@onready var direct_requests_list = $TabContainer/Opportunities/DirectRequests/RequestsList
@onready var marketplace_jobs_list = $TabContainer/Opportunities/MarketplaceJobs
@onready var tab_container = $TabContainer

func _ready():
	# Connect signals
	tab_container.connect("tab_changed", Callable(self, "on_tab_changed"))

	# Initial update
	update_dashboard()
	# Set the default tab to Overview
	tab_container.current_tab = 0  # 0 is the index of the Overview tab

func update_dashboard():
	update_company_info()
	update_weekly_summary()
	update_pipeline()
	update_news_alerts()
	update_ytd_summary()
	update_opportunities_list()

func update_company_info():
	if GameManager.company:
		company_name_label.text = GameManager.company.name
		business_type_label.text = GameManager.company.business_type
	else:
		company_name_label.text = "Unknown"
		business_type_label.text = "Unknown"

func update_weekly_summary():
	var latest_report = GameManager.weekly_reports[-1] if GameManager.weekly_reports else null
	if latest_report:
		weekly_summary.get_node("Revenue").text = "Revenue: $" + str(latest_report.revenue)
		weekly_summary.get_node("Expenses").text = "Expenses: $" + str(latest_report.expenses)
		weekly_summary.get_node("NetProfit").text = "Net Profit: $" + str(latest_report.net_profit)

func update_pipeline():
	# Remove all existing children from the pipeline
	for child in pipeline.get_children():
		child.queue_free()

	# Add new titles and progress bars for each active service job
	for job in ServiceSystems.active_service_jobs:
		var container = HBoxContainer.new()
		container.size_flags_horizontal = Control.SIZE_EXPAND_FILL

		var title_label = Label.new()
		title_label.text = job.opportunity.title
		title_label.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		title_label.add_theme_color_override("font_color", Color.BLACK)
		container.add_child(title_label)

		var progress_bar = ProgressBar.new()
		progress_bar.max_value = 1.0
		progress_bar.value = job.progress
		progress_bar.set_custom_minimum_size(Vector2(200, 20))
		progress_bar.size_flags_horizontal = Control.SIZE_SHRINK_END
		
		var style_box = StyleBoxFlat.new()
		style_box.bg_color = Color("#8ebef7")
		style_box.corner_radius_top_left = 4
		style_box.corner_radius_top_right = 4
		style_box.corner_radius_bottom_left = 4
		style_box.corner_radius_bottom_right = 4
		progress_bar.add_theme_stylebox_override("fill", style_box)
		
		var background_style = StyleBoxFlat.new()
		background_style.bg_color = Color("#d5d5d5")
		background_style.corner_radius_top_left = 4
		background_style.corner_radius_top_right = 4
		background_style.corner_radius_bottom_left = 4
		background_style.corner_radius_bottom_right = 4
		progress_bar.add_theme_stylebox_override("background", background_style)
		
		container.add_child(progress_bar)

		pipeline.add_child(container)

func update_news_alerts():
	# Remove all existing children from the news alerts
	for child in news_alerts.get_children():
		child.queue_free()

	for job in ServiceSystems.active_service_jobs:
		var weeks_left = job.opportunity.deadline - (TurnManager.current_week - job.start_week)
		if weeks_left == 1:
			var alert = Label.new()
			alert.text = "URGENT: " + job.opportunity.title + " due next week!"
			alert.add_theme_color_override("font_color", Color.RED)
			news_alerts.add_child(alert)
	# TODO: Add news headlines once market simulation is implemented

func update_ytd_summary():
	# TODO: Add YTD summary chart
	pass

func update_opportunities_list():
	# Remove all existing children from the direct requests list
	for child in direct_requests_list.get_children():
		child.queue_free()

	# Add new list items for each opportunity
	for i in range(ServiceSystems.opportunities.size()):
		var opp = ServiceSystems.opportunities[i]
		var item_container = HBoxContainer.new()
		
		var label = Label.new()
		label.text = "%s - Payout: $%d - Estimated Time: %d weeks - Deadline: Week %d" % [opp.title, opp.payout, opp.time_estimate, opp.deadline]
		item_container.add_child(label)
		
		var accept_button = Button.new()
		accept_button.text = "Accept"
		accept_button.connect("pressed", Callable(self, "_on_accept_request").bind(i))
		item_container.add_child(accept_button)
		
		direct_requests_list.add_child(item_container)

	# TODO: Add marketplace jobs list

func _on_tab_changed(tab):
	if tab == 1: # Assuming Opportunities is the second tab
		update_opportunities_list()

func _on_accept_request(index):
	if index >= 0 and index < ServiceSystems.opportunities.size():
		var opp_id = ServiceSystems.opportunities[index].id
		ServiceSystems.accept_opportunity(opp_id)
		update_opportunities_list()
		update_pipeline()
