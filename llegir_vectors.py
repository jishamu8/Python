#llegir vector
def llegir_vector():
	print("Dimensio del vector? ")
	n = int(input())
	v = []
	for i in range(n):
		print("Entra la component numero " + str(i+1) + ":")
		x = int(input())
		v.append(x)

	return v
