extends Node

var resolutions = [
    Vector2(1280, 720),
    Vector2(1366, 768),
    Vector2(1600, 900),
    Vector2(1920, 1080),
    Vector2(2560, 1440),
    Vector2(3840, 2160)
]



func _ready():
    set_process_input(true)
    