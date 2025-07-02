import json

class WaypointManager:
    def __init__(self):
        self.waypoints = []

    def add_waypoint(self, name, lat, lon):
        wp = {"name": name, "lat": lat, "lon": lon}
        self.waypoints.append(wp)

    def remove_waypoint(self, index):
        if 0 <= index < len(self.waypoints):
            del self.waypoints[index]

    def to_json(self):
        return json.dumps(self.waypoints, indent=4)

    def save_to_file(self, filename="waypoints.json"):
        with open(filename, 'w') as f:
            json.dump(self.waypoints, f, indent=4)

    def load_from_file(self, filename="waypoints.json"):
        with open(filename, 'r') as f:
            self.waypoints = json.load(f)