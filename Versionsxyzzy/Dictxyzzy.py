import time
yaxis = 0
xaxis = 0
zaxis = 5
items = {}
barriers = {}
items[torch] = False
items[bronzekey] = False
items[silverkey] = False
items[redpowder] = False
dead = False
barriers[doorone] = False
barriers[stairworms] = True
barriers[fountain] = False
def explodeydeath():
	if answer in ["use torch on bag","use bag on torch","use torch on leather bag","use leather bag on torch"]:
		if items[redpowder] == True and items[torch] == True:
			print("You blew up")
			global dead
			dead = True
def north():
	if answer in ["north","North","n","N","NORTH"]:
		global yaxis
		yaxis += 1
def south():
	if answer in ["south","South","s","S","SOUTH"]:
		global yaxis
		yaxis += -1
def west():
	if answer in ["west","West","W","w","WEST"]:
		global xaxis
		xaxis += -1
def east():
	if answer in ["east","East","E","e","EAST"]:
		global xaxis
		xaxis += 1
#==================================================================================================================================================
while dead == False:
	if zaxis == 5:
		if yaxis == 0 and xaxis == 0:
			answer = input("You are in a stone hallway. Go north or south? :")
			north()
			south()
	#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == 1 and xaxis == 0:
			if items[torch] == True and items[bronzekey] == True:
				answer = input("This is the northern balcony, it is mostly bare, but you can now see through the darkness, and the ground 10 feet below is made of writhing worms. Go south, or climb down?: ")
				south()
				if answer in ["climb down","jump down","jump","jump off","climb"]:
					dead = True
					print("You were eaten.")
			elif items[torch] == True and items[bronzekey] == False:
				answer = input("This is the northern balcony, it is mostly bare, but you can now see through the darkness, and the ground 10 feet below is made of writhing worms. The light lets you see a bronze key near the edge of the balcony. Go south, climb down, or take bronze key?: ")
				south()
				if answer in ["climb down","jump down","jump","jump off","climb"]:
					dead = True
					print("You were eaten.")
				if answer in ["take key","take bronze key"]:
					key = True
			elif items[torch] == False:
				answer = input("This is the northern balcony, it is mostly bare, and it is almost pitch black, however the ground seems only 10 feet down. Go south or climb down?: ")
				south()
				if answer in ["climb down","jump down","jump","jump off","climb"]:
					dead = True
					print("You were eaten.")
			explodeydeath()	#--------------------------------------------------------------------------------------------------------------------------------------------------
		elif yaxis == -1 and xaxis == 0:
			if items[torch] == True and items[bronzekey] == False:
				answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A fireplace sits with  cold coals agains the southern wall. Go west or north?: ")
				north()
				if answer in ["west","West","W","w"]:
					print("The door is locked.")
			elif items[torch] == True and items[bronzekey] == True:
				answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A fireplace sits with  cold coals agains the southern wall. Go west, north, or use bronze key?: ")
				north()
				if answer in ["west","West","W","w"] and barriers[doorone] == False:
					print("The door is locked.")
				if answer in ["west","West","W","w"] and barriers[doorone] == True:
					xaxis = xaxis - 1
				if answer in ["use key","use key on door", "use bronze key", "use bronze key on door"]:
					barriers[doorone] = True
					print("The door is open")
			elif items[torch] == False and items[bronzekey] == False:
				answer = input("This is the master bedroom. A large king-sized bed sits against the eastern wall. A small wooden stick half out of a fireplace burns in dim coals agains the southern wall. Go west, north, or take stick?: ")
				north()
				if answer in ["west","West","W","w"]:
					print("The door is locked")
				elif answer == "take stick":
					print("You have a torch, making the room brighter.")
					items[torch] = True
			explodeydeath()
	#--------------------------------------------------------------------------------------------------------------------------------------------------
		elif yaxis == -1 and xaxis == -1:
			answer = input("Another stone hallway with three exits to the north, east, and west. : ")
			north()
			west()
			east()
			explodeydeath()
	#--------------------------------------------------------------------------------------------------------------------------------------------------
		elif yaxis == 0 and xaxis == -1:
				if items[redpowder] == False:
					answer = input("This is a small personal alchemy lab. Chemicals, ingredients, and beakers are strewn across a stone table marked with large circular burns. A small leather bag with a fuse and a picture of a flame on it rests in the center. Go south, or take bag?: ")
					south()
					if answer in ["take bag","take leather bag"]:
						items[redpowder] = True
					if answer in ["take beaker","take beakers","take chemicals","take ingredients"]:
						print("Most of this stuff looks pretty dangerous, and you don't know what it all does. If only there was some safely contained marked bag.")
						items[redpowder] = True
				elif items[redpowder] == True:
					answer = input("This is a small personal alchemy lab. Chemicals, ingredients, and beakers are strewn across a stone table marked with large circular burns. Go south? : ")
					south()
					if answer in ["take beaker","take beakers","take chemicals","take ingredients"]:
						print("Most of this stuff looks pretty dangerous, and you don't know what it all does.")
				explodeydeath()
	#--------------------------------------------------------------------------------------------------------------------------------------------------
		elif yaxis == -1 and xaxis == -2:
			if barriers[stairworms] == True:
				answer = input("This is a staircase, but as you approach it you see that after the first flight of stairs, there is a floor of writhing worms covering the rest of the stairs. They seem to recoil as the light of the fire from your torch hits them. Go east, or use torch on something? : ")
				east()
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
					items[redpowder] = False
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
					barriers[stairworms] = False
			if barriers[stairworms] == False:
				answer = input("This ancient set of stone stairs spirals downward. Go down? : ")
				if answer in ["down","Down","d","D","Go down","go down"]:
					zaxis = zaxis - 1
#==================================================================================================================================================
	if zaxis == 4:
		if yaxis == -1 and xaxis == -1:
			south()
			west()
			east()
			answer = input("The stairs spiral further downward, but are covered with more worms. They too recoil from your torch. There are exits in all directions.")
			if doortwo == False:
				if answer in ["north","North","n","N","NORTH"]:
					print("It's locked")
			if doortwo == True:
				if answer in ["north","North","n","N","NORTH"]:
					global yaxis
					yaxis += 1
			if answer in ["use key","use silver key","use silver key on door","use silver key on north door"]:
				if items[silverkey] == True:
					not doortwo
					print("The north door opened")
				if items[silverkey] == False:
					print("The bronze key doesn't work.")
			if answer in ["use bronze key", "use bronze key on door", "use bronze key on north door"]:
				print("The bronze key doesn't work.")
			if answer in ["down","Down","d","D","Go down","go down"]:
					print("You were eaten")
					death = True
#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == 0 and xaxis == -1:
			pass
#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == -1 and xaxis == 0:
			answer = input("You are in the southwest corner of a massive chamber. The entire Northeast corner is taken up by a statue to a bright yellow deity.")
			north()
			west()
			east()
#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == 0 and xaxis == 0:
			pass
#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == -1 and xaxis == 1:
			answer = input("In the southeast, a strange stone tablet sits on a podium against the east wall. It reads LTHI, HDJIW, TPHI, TPHI, CDGIW, TPHI, HDJIW.")
#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == -2 and xaxis == -1:
			pass
#--------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == -1 and xaxis == -2:
			answer = input("A somewhat grand hallway decorated with stone carvings leads to the west corridoor. A small dirty maintenance door leads to the north. A wooden door to the east leads back to the staircase.")
			north()
			east()
			west()
			if answer in ["look","look at carvings","look at hallway","look around","look at walls","look at stone carvings"]:
				print("The carvings are of many things, people, trees, or simple geometric shapes, but they are all in groups of three.")
#---------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == 0 and xaxis == -2:
			answer = input("This small dark room is dominated by a large pipeline running from the west wall to the east wall. More of the worms and darkness are in this room, but seem to be avoiding the pipes as much as possible. There is one exit to the south.")
			south()
#---------------------------------------------------------------------------------------------------------------------------------------------------
		if yaxis == -1 and xaxis == -3:
			if barriers[fountain] == False:
				answer = input("This is a large church like room. A yellow ghostly figure floats above a large fountain. It is curled up like a small child, has long blonde hair, and seems to be sleeping. The fountain is completely dry. Worms cover the walls and shadows run deep in this room, but the light from the floating figure is holding them at bay. There is a single exit to the east.")
				east()
		
			


