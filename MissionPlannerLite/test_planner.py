import unittest
from planner import WaypointManager

class TestWaypointManager(unittest.TestCase):
    def test_add_waypoint(self):
        wm = WaypointManager()
        wm.add_waypoint("Test", 1.0, 2.0)
        self.assertEqual(len(wm.waypoints), 1)
        self.assertEqual(wm.waypoints[0]["name"], "Test")

    def test_remove_waypoint(self):
        wm = WaypointManager()
        wm.add_waypoint("A", 1, 1)
        wm.remove_waypoint(0)
        self.assertEqual(len(wm.waypoints), 0)

if __name__ == '__main__':
    unittest.main()