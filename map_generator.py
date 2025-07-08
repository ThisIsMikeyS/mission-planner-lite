import folium
import webbrowser
import os


def generate_map(waypoints, output_file="map.html"):
    """
    Generates an interactive map from a list of waypoints and opens it in a browser.
    """
    if not waypoints:
        return

    # Start with the first waypoint's location
    start = waypoints[0]
    map_obj = folium.Map(location=[start['lat'], start['lon']], zoom_start=6)

    for wp in waypoints:
        folium.Marker(
            location=[wp['lat'], wp['lon']],
            popup=wp['name'],
            icon=folium.Icon(color='blue')
        ).add_to(map_obj)

    # Draw lines between waypoints
    path = [(wp['lat'], wp['lon']) for wp in waypoints]
    folium.PolyLine(path, color="blue", weight=2.5, opacity=1).add_to(map_obj)

    # Save and open
    map_obj.save(output_file)
    webbrowser.open('file://' + os.path.realpath(output_file))
