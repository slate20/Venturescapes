extends Control

@onready var player_name_input = $Setup/VBoxContainer/PlayerNameInput
@onready var business_name_input = $Setup/VBoxContainer/BusinessName
@onready var manufacturing_type_option = $Setup/VBoxContainer/BusinessTypeSelect/Manufacturing
@onready var retail_type_option = $Setup/VBoxContainer/BusinessTypeSelect/Retail
@onready var service_type_option = $Setup/VBoxContainer/BusinessTypeSelect/Service
@onready var industry_option = $Setup/VBoxContainer/IndustrySelect
@onready var start_button = $Setup/VBoxContainer/StartButton

var business_type_options = []

func _ready():
	start_button.connect("pressed", Callable(self, "on_start_button_pressed"))

	# For now, we only have Web Development Agency as a business type
	industry_option.add_item("Web Development Agency")
	industry_option.select(0) # Select the first item

	# Set up business type options
	business_type_options = [manufacturing_type_option, retail_type_option, service_type_option]
	for option in business_type_options:
		option.connect("toggled", Callable(self, "on_business_type_toggled").bind(option))

func on_business_type_toggled(button_pressed, toggled_option):
	if button_pressed:
		for option in business_type_options:
			if option != toggled_option:
				option.set_pressed_no_signal(false)

func on_start_button_pressed():
	var player_name = player_name_input.text
	var business_name = business_name_input.text
	var business_industry = industry_option.get_item_text(industry_option.selected)
	
	var business_type = ""
	for option in business_type_options:
		if option.button_pressed:
			business_type = option.text
			break

	if business_type.is_empty():
		$ErrorLabel.text = "Please select a business type."
		return

	if player_name.strip_edges().is_empty():
		$ErrorLabel.text = "Please enter a name for your player."
		return

	if business_name.strip_edges().is_empty():
		$ErrorLabel.text = "Please enter a name for your business."
		return

	# Initialize the player and business in GameManager
	GameManager.initialize_player(player_name)
	GameManager.create_business(business_name, business_type, business_industry)

	# Change to the main game scene
	get_tree().change_scene_to_file("res://Scenes/main_layout.tscn")
