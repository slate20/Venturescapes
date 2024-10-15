# Godot Google Maps

Google Maps plugin for Godot 4.x using [Maps URLs](https://developers.google.com/maps/documentation/urls/get-started).

## Usage

### Location

Location is a class that combines the `query` and `place_id` fields into a
single object.

Use the following to create a new Location:

```gdscript
GMap.Location.new("London")
```

Use the following to specify location using latitude and longitude:

```gdscript
var location := GMap.Location.from_coord(51.507222, -0.1275)
```

### [Searching](https://developers.google.com/maps/documentation/urls/get-started#search-action)

To search for a location on a map and display results as pins:

```gdscript
var location := GMap.Location.new("London")
GMap.search(location)
```

### Directions

To get directions between two locations:

```gdscript
var origin := GMap.Location.new("London")
var destination := GMap.Location.new("Paris")
GMap.directions(origin, destination)
```

### Map

To display a map centered on a location:

```gdscript
# Eiffel Tower coordinates
var location := GMap.Location.from_coord(48.8584, 2.2945)
GMap.map(location)
```

### Street View

To display a street view of a location:

```gdscript
# Eiffel Tower coordinates
var location := GMap.Location.from_coord(48.8584, 2.2945)
GMap.street_view(location)
```
