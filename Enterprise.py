gradeaverage = open("Grade.txt","w")

name = input("What is your name?: ")

grade = 0
test_count = 0
test_sum = 0

while grade != -1:
	test_count = test_count+1
	test_sum = test_sum + grade
	grade=float(input("Enter your test Grades: "))

gradeaverage.write(name+"\n==================\n Average"+str(test_sum/test_count))
