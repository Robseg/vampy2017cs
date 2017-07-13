import random
def bubble(items):
	"""
	Sorts array from least to greatest in )(N**2) time
	Ex:
	>>> my_list = [2, 43, 78, 35, 27, 44, 9]
	>>> bubble(my_list)
	>>> my_list
	[2, 9, 27, 35, 43, 44, 78]
	"""
	for t in range(len(items)-1):
		for i in range(len(items)-1):
			if items[i] > items[i+1]:
				temp = items[i]
				items[i] = items[i+1]
				items[i+1] = temp
def reversebubble(items):
	"""
	Sorts array from greatest to least in )(N**2) time
	Ex:
	>>> my_list = [2, 43, 78, 35, 27, 44, 9]
	>>> bubble(my_list)
	>>> my_list
	[78, 44, 43, 35, 27, 9, 2]
	"""
	for t in range(len(items)-1):
		for i in range(len(items)-1):
			if items[i] < items[i+1]:
				temp = items[i]
				items[i] = items[i+1]
				items[i+1] = temp

def merge(items):
	#Base Case
	if len(items)<2:
		return

	#Cut Deck In Half
	mid = int(len(items) / 2)
	left  = []
	right = []
	for i in range(mid):
		left.append(items[i])

	for i in range(mid, len(items)):
		right.append(items[i])

	#Sort Halves
	merge(left)
	merge(right)

	#Zipper Halves Together
	L = 0
	R = 0
	M = 0

	while L < len(left) and R < len(right):
		if left[L] < right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	#Copy Everything Left From Left
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1

	#Copy Everything Left from the Right
	while R < len(right):
		items[M] = right[R]
		R += 1
		M += 1



def reversemerge(items):
	#Base Case
	if len(items)<2:
		return

	#Cut Deck In Half
	mid = int(len(items) / 2)
	left  = []
	right = []
	for i in range(mid):
		left.append(items[i])

	for i in range(mid, len(items)):
		right.append(items[i])

	#Sort Halves
	reverse_merge(left)
	reverse_merge(right)

	#Zipper Halves Together
	L = 0
	R = 0
	M = 0

	while L < len(left) and R < len(right):
		if left[L] > right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	#Copy Everything Left From Left
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1

	#Copy Everything Left from the Right
	while R < len(right):
		items[M] = right[R]
		R += 1
		M += 1
def merge(items):
	#Base Case
	if len(items)<2:
		return

	#Cut Deck In Half
	mid = int(len(items) / 2)
	left  = []
	right = []
	for i in range(mid):
		left.append(items[i])

	for i in range(mid, len(items)):
		right.append(items[i])

	#Sort Halves
	merge(left)
	merge(right)

	#Zipper Halves Together
	L = 0
	R = 0
	M = 0

	while L < len(left) and R < len(right):
		if left[L] < right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	#Copy Everything Left From Left
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1

	#Copy Everything Left from the Right
	while R < len(right):
		items[M] = right[R]
		R += 1
		M += 1

def shuffle(items):
	"""
	Shuffles the given items in O(N) time.
	>>> my_list = [1,2,3,4,5,6,7,8,9,10]
	>>>shuffle(my_list)
	>>> my_list
	[5,9,1,6,2,4,3,7,10,8]
	"""
	for i in range(len(items)):
		index        = random.randint(i, len(items)-1)
		temp         = items[i]
		items[i]     = items[index]
		items[index] = temp










