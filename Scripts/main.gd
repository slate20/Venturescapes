extends Control

# Onready variables for the UI elements
@onready var date_label = $MainLayout/TopBar/HBoxContainer/Date
@onready var days_left_label = $MainLayout/TopBar/HBoxContainer/HBoxContainer/DaysLeft
@onready var money_label = $MainLayout/TopBar/HBoxContainer/HBoxContainer/Money
@onready var reputation_label = $MainLayout/TopBar/HBoxContainer/HBoxContainer/Reputation
@onready var main_content = $MainLayout/MainContent
@onready var bottom_nav = $MainLayout/BottomNav/HBoxContainer
@onready var advance_week_button = $MainLayout/BottomNav/AdvanceWeekBtn
@onready var map_button = $MainLayout/BottomNav/MapBtn

# Dictionary to hold references to menu scenes
var views = {
	"Dashboard": preload("res://Scenes/Dashboard.tscn"),
	"Finances": preload("res://Scenes/Finances.tscn"),
	"Marketing": preload("res://Scenes/Marketing.tscn"),
	"HR": preload("res://Scenes/HR.tscn"),
	"RnD": preload("res://Scenes/RnD.tscn"),
	"Operations": preload("res://Scenes/Operations.tscn"),
	"Assets": preload("res://Scenes/Assets.tscn"),
	"Map": preload("res://Scenes/Map.tscn"),
}

func _ready():
	# Connect the navigation buttons
	for button in bottom_nav.get_children():
		button.connect("pressed", Callable(self, "_on_nav_button_pressed").bind(button.name))

	advance_week_button.connect("pressed", Callable(self, "_on_advance_week_pressed"))

	map_button.connect("pressed", Callable(self, "_on_map_button_pressed"))
	
	#Initialize UI
	update_ui()
	show_view("Dashboard")

func _on_nav_button_pressed(view_name):
	show_view(view_name)

func _on_map_button_pressed():
	show_view("Map")

func show_view(view_name):
	# Remove the current content
	for child in main_content.get_children():
		child.queue_free()

	# Instance and add the new content
	if views.has(view_name):
		var view_instance = views[view_name].instantiate()
		main_content.add_child(view_instance)
	else:
		print("View not found: ", view_name)

func update_ui():
	date_label.text = "Week %d, %d" % [TurnManager.current_week, TurnManager.current_year]
	days_left_label.text = "Days Left: %d" % TurnManager.days_left
	money_label.text = "Funds: %d" % GameManager.player.current_funds
	reputation_label.text = "Rep: %d%%" % GameManager.get_active_business().reputation

func _on_advance_week_pressed():
	TurnManager.advance_week()

	update_ui()


func take_action(action_days):
	if action_days <= TurnManager.days_left:
		TurnManager.days_left -= action_days
		update_ui()
		return true
	return false

# Call this function when an action is taken
func perform_action(action_days):
	if take_action(action_days):
		# Perform the action here
		print("Action performed over %d days" % action_days)
	else:
		print("Not enough days left to perform action")


# Called every frame. 'delta' is the elapsed time since the previous frame.
# func _process(delta):
# 	pass
