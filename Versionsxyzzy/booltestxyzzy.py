import time
yaxis = 0
xaxis = 0
zaxis = 5
dead = False
torch = False
key = False
doorone = False
redpowder = False
stairworms = True
def explodeydeath():
	if answer in ["use torch on bag","use bag on torch","use torch on leather bag","use leather bag on torch"]:
		if redpowder == True and torch == True:
			print("You blew up")
			dead = True
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while dead == False:
	if yaxis == 0 and xaxis == 0:
		answer = input("You are in a stone hallway with two exits. Go north, or south?: ")
		if answer in ["north","North","n","N"]:
				yaxis = yaxis + 1
		elif answer in ["south","South","s","S"]:
				yaxis = yaxis - 1
#--------------------------------------------------------------------------
	elif yaxis == 1 and xaxis == 0:
		if torch == True and key == True:
			answer = input("This is the northern balcony, it is mostly bare, but you can now see through the darkness, and the ground 10 feet below is made of writhing worms. Go south, or climb down?: ")
			if answer in ["south","South","s","S"]:
				yaxis = yaxis - 1
			elif answer in ["climb down","jump down","jump","jump off","climb"]:
				dead = True
				print("You were eaten.")
		elif torch == True and key == False:
			answer = input("This is the northern balcony, it is mostly bare, but you can now see through the darkness, and the ground 10 feet below is made of writhing worms. The light lets you see a key near the edge of the balcony. Go south, climb down, or take key?: ")
			if answer in ["south","South","s","S"]:
				yaxis = yaxis - 1
			elif answer in ["climb down","jump down","jump","jump off","climb"]:
				dead = True
				print("You were eaten.")
			elif answer in ["take key"]:
				key = True
		elif torch == False:
			answer = input("This is the northern balcony, it is mostly bare, and it is almost pitch black, however the ground seems only 10 feet down. Go south or climb down?: ")
			if answer in ["south","South","s","S"]:
				yaxis = yaxis - 1
			elif answer in ["climb down","jump down","jump","jump off","climb"]:
				dead = True
				print("You were eaten.")
#--------------------------------------------------------------------------
	elif yaxis == -1 and xaxis == 0:
		if torch == True and key == False:
			answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A fireplace sits with  cold coals agains the southern wall. Go west or north?: ")
			if answer in ["north","North","n","N"]:
				yaxis = yaxis + 1
			elif answer in ["west","West","W","w"]:
				print("The door is locked.")
		elif torch == True and key == True:
			answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A fireplace sits with  cold coals agains the southern wall. Go west, north, or use key?: ")
			if answer in ["north","North","n","N"]:
				yaxis = yaxis + 1
			elif answer in ["west","West","W","w"] and doorone == False:
				print("The door is locked.")
			elif answer in ["west","West","W","w"] and doorone == True:
				xaxis = xaxis - 1
			elif answer in ["use key","use key on door"]:
				doorone = True
				print("The door is open")
		elif torch == False and key == False:
			answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A small wooden stick half out of a fireplace burns in dim coals agains the southern wall. Go west, north, or take stick?: ")
			if answer in ["north","North","n","N"]:
				yaxis = yaxis + 1
			elif answer in ["west","West","W","w"]:
				print("The door is locked")
			elif answer == "take stick":
				print("You have a torch, making the room brighter.")
				torch = True
#--------------------------------------------------------------------------
	elif yaxis == -1 and xaxis == -1:
			answer = input("Another stone hallway with three exits to the north, east, and west. : ")
			if answer in ["north","North","n","N"]:
				yaxis = yaxis + 1
			elif answer in ["west","West","W","w"]:
				xaxis = xaxis -1
			elif answer in ["east","East","E","e"]:
				xaxis = xaxis + 1
#--------------------------------------------------------------------------
	elif yaxis == 0 and xaxis == -1:
			if redpowder == False:
				answer = input("This is a small personal alchemy lab. Chemicals, ingredients, and beakers are strewn across a stone table marked with large circular burns. A small leather bag with a fuse and a picture of a flame on it rests in the center. Go south, or take bag?: ")
				if answer in ["south","South","s","S"]:
					yaxis = yaxis - 1
				elif answer in ["take bag","take leather bag"]:
					redpowder = True
				elif answer in ["take beaker","take beakers","take chemicals","take ingredients"]:
					print("Most of this stuff looks pretty dangerous, and you don't know what it all does. If only there was some safely contained marked bag.")
				else:
					print("No")
					redpowder = True
			elif redpowder == True:
				answer = input("This is a small personal alchemy lab. Chemicals, ingredients, and beakers are strewn across a stone table marked with large circular burns. Go south? : ")
				if answer in ["south","South","s","S"]:
					yaxis = yaxis - 1
				elif answer in ["take beaker","take beakers","take chemicals","take ingredients"]:
					print("Most of this stuff looks pretty dangerous, and you don't know what it all does.")
				else:
					print("No")
#--------------------------------------------------------------------------
	elif yaxis == -1 and xaxis == -2:
		if stairworms == True:
			answer = input("This is a staircase, but as you approach it you see that after the first flight of stairs, there is a floor of writhing worms covering the rest of the stairs. They seem to recoil as the light of the fire from your torch hits them. Go east, or use torch on something? : ")
			if answer in ["east","East","E","e"]:
				xaxis = xaxis + 1
			if answer in ["down","Down","d","D","Go down","go down"]:
				print("You were eaten")
				death = True
			if answer in ["use torch","Use torch","Use torch on worms","use torch on worms"]:
				print("You wave your torch at the worms. They seem afraid of it, but as you get close they surge toward you. It seems the torch is too small to hurt them. You go back to the top.")
			if answer in ["use torch on bag","use torch on leather bag","Use torch on bag"]:
				print("You light the fuse")
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print("You drop the bag onto the worms")
				redpowder = False
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print("The bag explodes, and the worms screech and burn")
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print('.')
				time.sleep(0.5)
				print("The screeching shifts and sounds like a mirror shattering, and the worms crack apart and disappear. You can now go down the stairs")
				stairworms = False
		if stairworms == False:
			answer = input("This ancient set of stone stairs spirals downward. Go down?")
			if answer in ["down","Down","d","D","Go down","go down"]:
				zaxis = zaxis - 1



#--------------------------------------------------------------------------
