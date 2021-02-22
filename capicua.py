def capicua(v):
	n = len(v)
	for i in range(n//2):
		if v[i] != v[n-1-i]:
			return "no"
	return "si"