#Calcular el maxim del vector
def maxim(v):
	n = len(v)
	m = -1000
	p = -1
	for i in range(1,n):
		if v[i] > m:
			m = v[i]
			p = i 
                 

	return m,p