#vectors.py
#vectors.py
def capcalera():
        print("*******************************************")
        print("*Programa per fer operacions amb vectors")
        print("*")

def menu():
        print("\n")
        print("Les opcions desponibles son:\n")
        print("    1. Calcul del maxim d'un vector\n")
        print("    2. Calcul de la suma dels elements d'un vector\n")
        print("    3. Es capicua?\n")
        print("    4. Està ordenat?\n")
        print("    5. Sortir\n")
        print("\n")
        print("Entreu la vostra opcion:")
        o = int(input())
        return o

def vectors():
        capcalera()
        opcio = menu()
        while opcio != 5:
                vector = llegir_vector()
                if opcio == 1:
                        m = maxim(vector)
                        print("El maxim es " + str(m))
                elif opcio == 2: 
                        s = suma(vector)
                        print("La suma es " + str(s))
                elif opcio == 3: 
                        c = capicua(vector)
                        print((c)+ " Es capicua")           
                elif opcio == 4: 
                        o = ordenat(vector)
                        print((o) + " està ordenat")

                opcio = menu()
        print("adeu")

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

#Calcular la suma del vector
def suma(v):
	n = len(v)
	s = 0
	for i in range(n):
		s = s + v[i]
	return s

def igual1n(v):
  	if  v[0] == v[-1]:
  		return "Si"
  	else:
  		return "No"

def iguals12pu(v):
  	if  v[0] == v[-1] and v[1] == v[-2]:
  		return "Si"
  	else:
  		return "No"



def capicua(v):
	n = len(v)
	for i in range(n//2):
		if v[i] != v[n-1-i]:
			return "no"
	return "si"

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

def main():
	#vectors()

	vector = llegir_vector()
	print(vector)
	ord=ordenar(vector)
	print(str(ord))
'''	
	max,pos = maxim(vector)  
	print("la maxim dels volors es " + str(max) + " i la posicio es " +  str(pos))
	sum = suma(vector)
	print("La suma dels valors entrats es " + str(sum))
	ret=igual(vector)
	print (ret)
	ret_2=iguals12pu(vector)
	print (ret_2)
	ret_cap=capicua(vector)
	print (ret_cap)
'''	
main()
