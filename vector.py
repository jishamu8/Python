'''
Exercici 3: Feu un programa vectors() que mostri lo següent:


************************
* Programa per fer operacions amb vectors
*

Les opcions son:
	1. Calcular el maxim d'un vector
	2. Calcular la suma dels elements d'un vector
	3. Sortir
'''	
#vectors.py
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
	for i in range(n):
			if v[i] > m:
				m = v[i]

	return m

def suma(v):
    n = len(v)
    s = 0
    for i in range(n):
            s = s + v[i]
    return s

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
                        print("El maxim es " + str (m))
                if opcio == 2: 
                        s = suma(vector)
                        print("La suma es " + str (s))

                opcio = menu()
        print("adeu")



def main():
	vectors()



	
'''	vector = llegir_vector()
	print(vector)
	max = maxim(vector)
	print("la maxim dels volors es " + str(max))

	sum = suma(vector)
	print("La suma dels valors entrats es " + str(sum))

main()
'''
