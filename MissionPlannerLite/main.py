import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from planner import WaypointManager
from map_generator import generate_map



class MissionPlannerGUI:
    """
    A graphical interface for managing waypoints in a mission planning tool.
    """

    def __init__(self, root):
        """Initializes the GUI and sets up the layout."""
        self.root = root
        self.root.title("Mission Planner Lite")

        self.manager = WaypointManager()

        # Input fields
        self.name_var = tk.StringVar()
        self.lat_var = tk.StringVar()
        self.lon_var = tk.StringVar()
        self.alt_var = tk.StringVar()

        # GUI Layout
        tk.Label(root, text="Name:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(root, text="Latitude:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.lat_var).grid(row=1, column=1)

        tk.Label(root, text="Longitude:").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.lon_var).grid(row=2, column=1)

        tk.Label(root, text="Altitude (m):").grid(row=3, column=0)
        tk.Entry(root, textvariable=self.alt_var).grid(row=3, column=1)

        tk.Button(root, text="Add Waypoint", command=self.add_waypoint).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Export to JSON", command=self.export_waypoints).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Show Map", command=self.show_map).grid(row=6, column=0, columnspan=2)
        tk.Button(root, text="Calculate Flight Time", command=self.calc_time).grid(row=7, column=0, columnspan=2)

        # Listbox for displaying waypoints
        self.waypoint_list = tk.Listbox(root)
        self.waypoint_list.grid(row=8, column=0, columnspan=2)

        tk.Button(root, text="Delete Selected", command=self.delete_waypoint).grid(row=9, column=0, columnspan=2)

    def add_waypoint(self):
        """Handles the event for adding a new waypoint from user input."""
        try:
            name = self.name_var.get()
            lat = float(self.lat_var.get())
            lon = float(self.lon_var.get())
            alt = float(self.alt_var.get() or 0)
            self.manager.add_waypoint(name, lat, lon, alt)
            self.update_listbox()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric coordinates and altitude.")

    def delete_waypoint(self):
        """Handles deletion of the selected waypoint in the listbox."""
        sel = self.waypoint_list.curselection()
        if sel:
            self.manager.remove_waypoint(sel[0])
            self.update_listbox()

    def export_waypoints(self):
        """Exports the list of waypoints to a JSON file."""
        self.manager.save_to_file()
        messagebox.showinfo("Export", "Waypoints exported to waypoints.json")

    def calc_time(self):
        """ Handles calculation of estimated flight time. """
        if not self.manager.waypoints or len(self.manager.waypoints) < 2:
            messagebox.showinfo("Not Enough Data", "At least two waypoints are required.")
            return
        try:
            speed_kmh = simpledialog.askfloat("Flight Speed", "Enter speed in km/h:")
            if speed_kmh is None:
                return
            hours = self.manager.estimate_flight_time(speed_kmh)
            minutes = hours * 60
            messagebox.showinfo("Estimated Flight Time", f"Total distance: {self.manager.total_distance_km():.2f} km\nEstimated time: {minutes:.1f} minutes")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_listbox(self):
        """Refreshes the listbox to display current waypoints."""
        self.waypoint_list.delete(0, tk.END)
        for i, wp in enumerate(self.manager.waypoints):
            entry = f"{i + 1}. {wp['name']} ({wp['lat']}, {wp['lon']})"
            self.waypoint_list.insert(tk.END, entry)

    def show_map(self):
        """Displays the current waypoints on an interactive OpenStreetMap map."""
        if not self.manager.waypoints:
            messagebox.showwarning("No Data", "No waypoints to display on map.")
            return
        generate_map(self.manager.waypoints)


if __name__ == "__main__":
    root = tk.Tk()
    app = MissionPlannerGUI(root)
    root.mainloop()


