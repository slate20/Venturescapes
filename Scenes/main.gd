extends Control

# Onready variables for the UI elements
@onready var date_label = $MainLayout/TopBar/HBoxContainer/Date
@onready var days_left_label = $MainLayout/TopBar/HBoxContainer/HBoxContainer/DaysLeft
@onready var money_label = $MainLayout/TopBar/HBoxContainer/HBoxContainer/Money
@onready var reputation_label = $MainLayout/TopBar/HBoxContainer/HBoxContainer/Reputation
@onready var main_content = $MainLayout/MainContent
@onready var bottom_nav = $MainLayout/BottomNav/HBoxContainer
@onready var advance_week_button = $MainLayout/BottomNav/AdvanceWeekBtn


# Game state variables
var current_week = 1
var current_year = 2024
var days_left = 7
var money = 10000
var reputation = 68


# Dictionary to hold references to menu scenes
var views = {
	"Dashboard": preload("res://Scenes/Dashboard.tscn"),
	"Finances": preload("res://Scenes/Finances.tscn"),
	"Marketing": preload("res://Scenes/Marketing.tscn"),
	"HR": preload("res://Scenes/HR.tscn"),
	"RnD": preload("res://Scenes/RnD.tscn"),
	"Operations": preload("res://Scenes/Operations.tscn"),
	"Assets": preload("res://Scenes/Assets.tscn"),
}


# Called when the node enters the scene tree for the first time.
func _ready():
	# Connect the navigation buttons
	for button in bottom_nav.get_children():
		button.connect("pressed", Callable(self, "_on_nav_button_pressed").bind(button.name))

	advance_week_button.connect("pressed", Callable(self, "_on_advance_week_pressed"))

	# Initialize UI
	update_ui()
	show_view("Dashboard")

func _on_nav_button_pressed(view_name):
	show_view(view_name)

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
	date_label.text = "Week %d, %d" % [current_week, current_year]
	days_left_label.text = "Days Left: %d" % days_left
	money_label.text = "Funds: %d" % money
	reputation_label.text = "Rep: %d%%" % reputation

func _on_advance_week_pressed():
	advance_week()

func advance_week():
	current_week += 1
	days_left = 7
	if current_week > 52:
		current_week = 1
		current_year += 1

	# TODO: Implement week-based logic (costs, revenues, reputation change, etc.)

	update_ui()


func take_action(action_days):
	if action_days <= days_left:
		days_left -= action_days
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
