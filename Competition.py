#def max_partition_sum(S,K):
#	if K == 1:
#		return int(S)
#	else:
#		maxSum = 0
#		i = 1
#		while Z <= 100 and i < len(S):
#			tmpSum = Z + max_partition_sum(S[i:], K-1)
#			if tmpSum > maxSum:
#				maxSum = tmpSum
#
#			i += 1
#			Z = int(S[:i])
#		return
#
#filename = "..."
#fp = open(filename, "r")
#C = int(fp.readline())
#for t in range(C):
#	line = fp.readline().strip()
#	data = line.split()
#	K = int(data[0])
#	S = data[1]
#	print(round(max_partition_sum(S, K) / K))




def landHo():
	filename = "/home/vampy/data/Islandarrays"
	fp = open(filename, "r")
	M = int(fp.readline())
	F = 0
	while F < M:
		array = fp.readline().strip().split()
		X = 0
		K = 1
		while (K <= 13):
			if (int(array[K+1])) == (int(array[K])+1):
				X += 1
			K +=1
		F += 1
		print(str(F)+" "+str(X)+"\n")


def Prob1(K):
	let = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
	X = 0
	def Subsol(K, Q):
		if X <= K:
			while Q < 25:
				print(let[Q])
				Q += 1
				Subsol(K, Q)
	if K < 26:
		for i in range(K):
			Subsol(K, 0)

			











#if K == 1:
#		Q = 0
#		while Q < 26:
#			print(let[P])
#			Q += 1 
#	if K == 2:
#		Q = 0
#		W = 1
#		while Q < 26:
#			while W < 26:
#				print(let[Q]+let[P])
#				W += 1
#			Q += 1 
#			W += 1
#
#Prob1(2)


	
 





		
		

