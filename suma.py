#Calcular la suma del vector
def suma(v):
	n = len(v)
	s = 0
	for i in range(n):
		s = s + v[i]
	return s
