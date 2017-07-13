lower = 0
upper = 0
guess = 1
ans = ""
while ans != "YEPP":
	ans = input("Is "+str(guess)+" your number or should I go less or more? (YEPP/LESS/MORE): ")
	if ans == "MORE":
		if upper == 0:
			guess *= 2
		else:
			lower = guess
			guess = int((lower + upper)/2)
	elif ans == "LESS":
		if upper == 0:
			lower = int(guess / 2)
		upper = guess
		guess = int((lower + upper)/2)
print("Woohoo I found your number and it is "+str(guess)+"!")
