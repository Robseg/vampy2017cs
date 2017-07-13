yaxis = 0
xaxis = 0
dead = 0
torch = 0
key = 0
doorone = 0
while dead == 0:
	if yaxis == 0 and xaxis == 0:
			answer = input("You are in a stone hallway with two exits. Go north, or south?: ")
			if answer == "north":
				yaxis = yaxis + 1
			elif answer == "south":
				yaxis = yaxis - 1
#--------------------------------------------------------------------------
	elif yaxis == 1 and xaxis == 0:
		if torch == 1 and key == 1:
			answer = input("This is the northern balcony, it is mostly bare, but you can now see through the darkness, and the ground 10 feet below is made of writhing worms. Go south, or climb down?: ")
			if answer == "south":
				yaxis = yaxis - 1
			elif answer == "climb down":
				dead = 1
				print("You were eaten.")
		elif torch == 1 and key == 0:
			answer = input("This is the northern balcony, it is mostly bare, but you can now see through the darkness, and the ground 10 feet below is made of writhing worms. The light lets you see a key near the edge of the balcony. Go south, climb down, or take key?: ")
			if answer == "south":
				yaxis = yaxis - 1
			elif answer == "climb down":
				dead = 1
				print("You were eaten.")
			elif answer == "take key":
				key = 1
		elif torch == 0:
			answer = input("This is the northern balcony, it is mostly bare, and it is almost pitch black, however the ground seems only 10 feet down. Go south or climb down?: ")
			if answer == "south":
				yaxis = yaxis - 1
			elif answer == "climb down":
				dead = 1
				print("You were eaten.")
#--------------------------------------------------------------------------
	elif yaxis == -1 and xaxis == 0:
		if torch == 1 and key == 0:
			answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A fireplace sits with  cold coals agains the southern wall. Go west or north?: ")
			if answer == "north":
				yaxis = yaxis + 1
			elif answer == "west" and key == 0:
				print("The door is locked.")
			elif answer == "west" and key == 1:
				xaxis = xaxis - 1
		elif torch == 1 and key == 1:
			answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A fireplace sits with  cold coals agains the southern wall. Go west, north, or use key?: ")
			if answer == "north":
				yaxis = yaxis + 1
			elif answer == "west" and doorone == 0:
				print("The door is locked.")
			elif answer == "west" and doorone == 1:
				xaxis = xaxis - 1
			elif answer == "use key":
				doorone = 1
				print("The door is open")
		elif torch == 0 and key == 0:
			answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A small wooden stick half out of a fireplace burns in dim coals agains the southern wall. Go west, north, or take stick?: ")
			if answer == "north":
				yaxis = yaxis + 1
			elif answer == "west":
				print("The door is locked")
			elif answer == "take stick":
				print("You have a torch, making the room brighter.")
				torch = 1
#--------------------------------------------------------------------------
	elif yaxis == -1 and xaxis == -1:
			answer = input("Another stone hallway with three exits. Go east, north, or west?: ")
			if answer == "north":
				yaxis = yaxis + 1
			elif answer == "west":
				xaxis = xaxis -1
			elif answer == "east":
				xaxis = xaxis + 1







