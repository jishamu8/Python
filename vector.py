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
        print("    3. Sortir\n")
        print("\n")
        print("Entreu la vostra opcion:")
        o = int(input())
        return o

def vectors():
        capcalera()
        opcio = menu()
        while opcio != 3:
                vector = llegir_vector()
                if opcio == 1:
                        m = maxim(vector)
                        print("El maxim es " + str(m))
                elif opcio == 2: 
                        s = suma(vector)
                        print("La suma es " + str(s))

                opcio = menu()
        print("adeu")


def llegir_vector():
	print("Dimensio del vector? ")
	n = int(input())
	v = []
	for i in range(n):
		print("Entra la component numero " + str(i+1) + ":")
		x = int(input())
		v.append(x)

	return v



def maxim(v):
	n = len(v)
	m = -1000
	p = -1
	for i in range(1,n):
		if v[i] > m:
			m = v[i]
			p = i 
                 

	return m,p

def suma(v):
	n = len(v)
	s = 0
	for i in range(n):
		s = s + v[i]
	return s

def igual(g):
  	if  g[0] == g[-1]:
  		return "Si, primer i ultim son igual"
  	else:
  		return "No, primer i ultim son igual"

def igual_2(g_2):
  	if  g_2[0] == g_2[-1] and g_2[1] == g_2[-2]:
  		return "Si, primer i ultim son igual, segon i penultim son iguals "
  	else:
  		return "No,  primer i ultim son igual, segon i penultim son iguals "



def main():
#	vectors()
	
	vector = llegir_vector()
	print(vector)
	max,pos = maxim(vector)
    
	print("la maxim dels volors es " + str(max) + " i la posicio es " +  str(pos))
	sum = suma(vector)
	print("La suma dels valors entrats es " + str(sum))
	ret=igual(vector)
	print (ret)
	ret_2=igual_2(vector)
	print (ret_2)
	
main()
