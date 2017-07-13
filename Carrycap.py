
def capacity(K, weights)
		if sum(weights) < K:
			return None
		weights = sorted(weights, reverse=true)

		def solve(K, i):
			print("solve({0}, {1})".format(K, i))
			if K == 0:
				return []

			if sum([weights[w] for w in range(i, len(weights

			while i < len(weights) and weights[i] > K:
				i += 1

			if i == len(weights):
				return None
		
			subK = K - weights[i]
			subI = i + 1
			subsolution = solve(subK, subI)
			if subsolution is not None:
				subsolution.append(weights[i])
				return subsolution
		
			subsolution = solve(K, subI)
			if subsolution is not None:
			return  subsolution
	
		return None

	return solve(K, 0)

print(capacity(2000, [x**2 for x in range(100)]))































