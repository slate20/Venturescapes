extends Control

var dragging = false
var drag_start_pos = Vector2.ZERO
var zoom_level = 1.0
var zoom_speed = 0.1
var min_zoom = 0.5
var max_zoom = 2.0

func _ready():
    # Ensure the map is centered initially
    center_map()

func _gui_input(event):
    if event is InputEventMouseButton:
        if event.button_index == MOUSE_BUTTON_LEFT:
            if event.pressed:
                dragging = true
                drag_start_pos = event.position
            else:
                dragging = false
        elif event.is_pressed():
            if event.button_index == MOUSE_BUTTON_WHEEL_UP:
                zoom(1 + zoom_speed, event.position)
            elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
                zoom(1 - zoom_speed, event.position)
    elif event is InputEventMouseMotion and dragging:
        var drag_delta = event.position - drag_start_pos
        $Map.position += drag_delta
        drag_start_pos = event.position
        
        # Clamp the map position to keep it within bounds
        clamp_map_position()

func center_map():
    var map_size = $Map.texture.get_size() * zoom_level
    var container_size = size
    $Map.position = (container_size - map_size) / 2

func clamp_map_position():
    var map_size = $Map.texture.get_size() * zoom_level
    var container_size = size
    
    $Map.position.x = clamp($Map.position.x, container_size.x - map_size.x, 0)
    $Map.position.y = clamp($Map.position.y, container_size.y - map_size.y, 0)

func zoom(factor, mouse_position):
    var old_zoom = zoom_level
    zoom_level = clamp(zoom_level * factor, min_zoom, max_zoom)
    
    if zoom_level != old_zoom:
        var mouse_offset = mouse_position - $Map.position
        var new_mouse_offset = mouse_offset * (zoom_level / old_zoom)
        $Map.position += mouse_offset - new_mouse_offset
        
        $Map.scale = Vector2.ONE * zoom_level
        clamp_map_position()
