robot_name = "Robo1"

def check_robot(battery, distance ,temperature,speed):
	print("Robot:", robot_name)
	print("Battery:",battery, "%")
	print("Obstacle distance:",distance,"m")
	print("Temperature:", temperature, "C")
	print("Speed:", speed, "km/hr")

	if battery <=20:
		print("Low battery - STOP")
	elif distance <=2:
		print("OBSTACLE DETECTED -STOP")
	elif temperature >50:
		print("OVERHEATING -STOP")
	else:
		print("PATH CLEAR -MOVE")
	if speed >10:
		print("Speed too high -SLOW DOWN")

check_robot(10,5,30,15)
