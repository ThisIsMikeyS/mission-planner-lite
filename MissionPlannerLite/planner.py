import json
from math import radians, sin, cos, sqrt, atan2


class WaypointManager:
    """Manages a list of waypoints with distance and time calculation support."""

    def __init__(self):
        self.waypoints = []

    def add_waypoint(self, name, lat, lon, alt=0):
        """Adds a waypoint with optional altitude."""
        wp = {"name": name, "lat": lat, "lon": lon, "alt": alt}
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

    def total_distance_km(self):
        """Calculates total 3D flight path distance in kilometers."""
        total = 0.0
        for i in range(1, len(self.waypoints)):
            wp1 = self.waypoints[i - 1]
            wp2 = self.waypoints[i]
            total += self._haversine_3d(wp1, wp2)
        return total

    def estimate_flight_time(self, speed_kmh):
        """Estimates total flight time in hours given speed in km/h."""
        distance = self.total_distance_km()
        return distance / speed_kmh if speed_kmh > 0 else 0

    def _haversine_3d(self, wp1, wp2):
        """Calculates 3D haversine distance considering altitude."""
        R = 6371  # Earth radius in km
        lat1, lon1, alt1 = radians(wp1['lat']), radians(wp1['lon']), wp1.get('alt', 0)
        lat2, lon2, alt2 = radians(wp2['lat']), radians(wp2['lon']), wp2.get('alt', 0)

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        ground_dist = R * c
        alt_diff_km = abs(alt2 - alt1) / 1000  # meters to km
        return sqrt(ground_dist**2 + alt_diff_km**2)