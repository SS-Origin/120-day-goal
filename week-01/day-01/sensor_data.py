sensor_readings = [50,25,80,15,40]

print("Sensor readings:")

for distance in sensor_readings:
	print(distance, "cm")

	if distance < 30:
		print("OBSTACLE! STOP")
	else:
		print("Path clear - MOVE")
	print()
