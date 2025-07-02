import json


class WaypointManager:
    """
    Manages a list of waypoints for a mission planner.
    Provides functionality to add, remove, load, and save waypoints.
    """

    def __init__(self):
        """Initializes an empty list of waypoints."""
        self.waypoints = []

    def add_waypoint(self, name, lat, lon):
        """Adds a new waypoint with the given name, latitude, and longitude."""
        wp = {"name": name, "lat": lat, "lon": lon}
        self.waypoints.append(wp)

    def remove_waypoint(self, index):
        """Removes a waypoint by index if within valid range."""
        if 0 <= index < len(self.waypoints):
            del self.waypoints[index]

    def to_json(self):
        """Returns the waypoints list as a JSON string."""
        return json.dumps(self.waypoints, indent=4)

    def save_to_file(self, filename="waypoints.json"):
        """Saves the current waypoints to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.waypoints, f, indent=4)

    def load_from_file(self, filename="waypoints.json"):
        """Loads waypoints from a JSON file."""
        with open(filename, 'r') as f:
            self.waypoints = json.load(f)