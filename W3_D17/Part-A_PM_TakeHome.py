"""
Day 17 · PM Session · Take-Home Assignment
Part A: Concept Application — Sensor Array Analytics Dashboard
"""

import numpy as np

# 1. Generate the dataset: shape (50, 24, 3)
# Temperature: 15-45C, Humidity: 20-95%, Battery: 10-100%
np.random.seed(1313)
sensors = np.zeros((50, 24, 3))
sensors[:, :, 0] = np.random.uniform(15, 45, size=(50, 24))  # Temp
sensors[:, :, 1] = np.random.uniform(20, 95, size=(50, 24))  # Humidity
sensors[:, :, 2] = np.random.uniform(10, 100, size=(50, 24)) # Battery

# 2. Identify 'alert sensors': temp > 40C OR humidity > 90% in ANY hour
alert_mask = (sensors[:, :, 0] > 40) | (sensors[:, :, 1] > 90)
alert_sensors = np.where(np.any(alert_mask, axis=1))[0]
print(f"Alert sensors: {alert_sensors.tolist()}")

# 3. Calculate per-sensor daily averages for all 3 metrics
daily_averages = np.mean(sensors, axis=1) # (50, 3)
print(f"Daily averages shape: {daily_averages.shape}")

# 4. Find the hour with highest average temperature across all sensors
# Average temp across sensors for each hour
avg_temp_per_hour = np.mean(sensors[:, :, 0], axis=0) # (24,)
hottest_hour = np.argmax(avg_temp_per_hour)
print(f"Hottest hour: {hottest_hour} (Time: {hottest_hour}:00)")

# 5. Battery drain analysis: compute battery drop (first hour - last hour)
first_hour_battery = sensors[:, 0, 2]
last_hour_battery = sensors[:, -1, 2]
battery_drain = first_hour_battery - last_hour_battery
critical_drain_sensors = np.where(battery_drain > 50)[0]
print(f"Sensors with critical battery drain: {critical_drain_sensors.tolist()}")

# 6. Normalize ALL metrics to [0,1] range per metric
# Min and max across all sensors and all hours for each metric
s_min = sensors.min(axis=(0, 1), keepdims=True)
s_max = sensors.max(axis=(0, 1), keepdims=True)
normalized_sensors = (sensors - s_min) / (s_max - s_min)

# 7. Save the daily averages as sensor_summary.csv with header
header = "Temperature,Humidity,Battery"
np.savetxt("sensor_summary.csv", daily_averages, delimiter=",", header=header, comments="")
print("Saved sensor_summary.csv")

# Verification of normalization
print(f"\nVerification - Normalized Temp range: [{normalized_sensors[:,:,0].min():.2f}, {normalized_sensors[:,:,0].max():.2f}]")
