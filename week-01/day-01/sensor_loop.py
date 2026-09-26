battery = 100

for reading in range(5):
	distance = int(input("Enter obstacle distance(cm): "))

	print("Sensor reading:",distance, "cm")

	if distance < 30:
		print("OBSTACLE! STOP")
	else:
		print("Path clear - MOVE")

	battery -= 5
	print("Battery:",battery,"%")
	print()
