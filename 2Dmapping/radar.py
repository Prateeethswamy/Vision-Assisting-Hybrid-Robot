
import serial
import numpy as np
import matplotlib.pyplot as plt

PORT = "COM15"   # CHANGE THIS
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)
plt.ion()
fig, ax = plt.subplots()

ax.set_xlim(-500, 500)
ax.set_ylim(-500, 500)
ax.set_title("Persistent 2D Ultrasonic Mapping")
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")

# Persistent storage
x1_list, y1_list = [], []
x2_list, y2_list = [], []

while True:
    try:
        line = ser.readline().decode().strip()
        if not line:
            continue

        data = line.split(",")

        if len(data) != 4:
            continue

        angle1 = float(data[0])
        dist1 = float(data[1])
        angle2 = float(data[2])
        dist2 = float(data[3])

        # FRONT SENSOR (normal)
        theta1 = np.radians(angle1)
        x1 = dist1 * np.cos(theta1)
        y1 = dist1 * np.sin(theta1)

        # REAR SENSOR (shift 180 degrees)
        theta2 = np.radians(angle2 + 180)
        x2 = dist2 * np.cos(theta2)
        y2 = dist2 * np.sin(theta2)

        x1_list.append(x1)
        y1_list.append(y1)

        x2_list.append(x2)
        y2_list.append(y2)

        ax.clear()
        ax.set_xlim(-500, 500)
        ax.set_ylim(-500, 500)
        ax.set_title("Persistent 2D Ultrasonic Mapping")

        # Continuous lines
        ax.plot(x1_list, y1_list, linewidth=2, color='blue', label="Front Sensor")
        ax.plot(x2_list, y2_list, linewidth=2, color='red', label="Rear Sensor")

        ax.legend()
        ax.grid(True)

        plt.pause(0.01)

    except:
        pass
