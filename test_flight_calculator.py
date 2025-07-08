import unittest
from planner import WaypointManager


class TestFlightCalculator(unittest.TestCase):
    """
    Tests for the estimated flight time functionality.
    """
    def test_distance_and_time(self):
        """Test adding two waypoints and calculating the correct distance ans estimated flight time."""
        wm = WaypointManager()
        wm.add_waypoint("A", 51.5, -0.1, 100)
        wm.add_waypoint("B", 52.0, 0.1, 200)
        dist = wm.total_distance_km()
        self.assertTrue(dist > 0)
        time = wm.estimate_flight_time(100)
        self.assertAlmostEqual(time, dist / 100, places=4)


if __name__ == '__main__':
    unittest.main()