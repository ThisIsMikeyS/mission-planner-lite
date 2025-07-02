import unittest
import os
from map_generator import generate_map


class TestMapGenerator(unittest.TestCase):
    """
    Tests for the map generation functionality using Folium.
    """

    def test_generate_map_creates_file(self):
        """Ensure the map file is created for valid waypoints."""
        waypoints = [
            {"name": "Test A", "lat": 51.5, "lon": -0.1},
            {"name": "Test B", "lat": 52.0, "lon": 0.1}
        ]
        filename = "test_map.html"
        generate_map(waypoints, output_file=filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()