def ordenat(v):
	n=len(v)
	for i in range(n-2):
		if v[i] >= v[i+1]:
			return "no"
	return "si"
 

def ordenar(v):
        n = len(v)
        for i in range(n):
                for j in range(n):
                        if i<j:
#                          si i<j es cierto quiere ecir que el elemento v[i]
#                          es anterior a v[j] -> si además v[i] > v[j]
                                if v[i] > v[j]:
                                        aux = v[i]
                                        v[i] = v[j]
                                        v[j] = aux

        return v