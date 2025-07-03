
# 🗺️ Mission Planner Lite

**Mission Planner Lite** is a lightweight, desktop-based waypoint management tool built with Python and Tkinter. Designed to simulate basic mission or route planning functionality, this application allows users to input, view, and export waypoints in a clean and user-friendly interface.

> Built for learning, demonstration, and portfolio development — no proprietary code, no NDA restrictions.

---

## 📸 Screenshots

### 🧼 Tool GUI
![GUI Screenshot](images/gui-screenshot.png)

### 🗺️ Display Map
![Display Map Screenshot](images/map-screenshot.png)

---

## ✨ Features

- 🧭 Add, view, and delete named waypoints with latitude, longitude, and altitude (in meters)
- 📤 Export waypoint lists to `.json` format
- 🗺️ View waypoints on an interactive OpenStreetMap map (opens in browser)
- ⏱ Estimate total flight time based on user-defined speed and waypoint distances (3D)
- 🧼 Simple GUI using Python Tkinter (fixed layout, scrollable)
- ✅ Includes unit tests for core logic, map rendering, and distance/time calculations

---

## 📁 Project Structure

```
mission_planner_lite/
├── main.py # GUI code
├── planner.py # Waypoint logic handler
├── map_generator.py # Folium-based map rendering
├── test_planner.py # Unit tests for waypoint logic
├── test_map_generator.py # Unit test for map creation
├── test_flight_calculator.py # Unit test for flight distance/time
├── waypoints.json # Sample export file
├── requirements.txt # Project dependencies
├── README.md # Project overview (this file)
├── LICENSE # MIT License
└── images/
└── gui-screenshot.png # GUI image for GitHub preview
└── map-screenshot.png # Display map image for GitHub preview
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Windows 11 (or other OS with Python 3.10+)
- [Python 3.10+](https://www.python.org/downloads/)
- Tkinter (usually bundled with Python on Windows)

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ThisIsMikeyS/mission-planner-lite.git
   cd mission-planner-lite
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install tk folium
   ```

---

## ▶️ Running the App

To start the GUI:
```bash
python main.py
```

Once the GUI is running, you can:
- Add or delete waypoints (with optional altitude)
- Export waypoints to `waypoints.json`
- Click **Show Map** to open a visual map in your web browser with markers and paths
- Click **Calculate Flight Time** to estimate total mission duration based on your input speed (in km/h)

---

## 🧪 Running Tests

To run the unit tests:
```bash
python test_planner.py
```

Expected output:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

---

## 💾 Sample Output (`waypoints.json`)
```json
[
  {
    "name": "Alpha",
    "lat": 51.5074,
    "lon": -0.1278
  },
  {
    "name": "Bravo",
    "lat": 52.2053,
    "lon": 0.1218
  }
]
```

---

## 🛠️ Future Improvements

- Import/export CSV
- Path visualization
- REST API or local DB support

---

## 📚 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 🧑‍💻 Author

**Michael Saunders**  
Freelance Software & Systems Developer | Technical Writer  
[LinkedIn](https://www.linkedin.com/in/michael-saunders-805785128/) · [GitHub](https://github.com/ThisIsMikeyS)

---
