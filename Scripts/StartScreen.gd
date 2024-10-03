extends Control

@onready var company_name_input = $Setup/VBoxContainer/CompanyName
@onready var business_type_option = $Setup/VBoxContainer/BusinessSelect
@onready var start_button = $Setup/VBoxContainer/StartButton

func _ready():
	start_button.connect("pressed", Callable(self, "on_start_button_pressed"))

	# For now, we only have Web Development Agency as a business type
	business_type_option.add_item("Web Development Agency")
	business_type_option.select(0) # Select the first item

func on_start_button_pressed():
	var company_name = company_name_input.text
	var business_type = business_type_option.get_item_text(business_type_option.selected)

	if company_name.strip_edges().is_empty():
		# Show an error message if the company name is empty
		$ErrorLabel.text = "Please enter a company name."
		return

	# Initialize the company in GameManager
	GameManager.initialize_company(company_name, business_type)

	# Change to the main game scene
	get_tree().change_scene_to_file("res://Scenes/main_layout.tscn")
