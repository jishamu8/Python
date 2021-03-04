#imports
from capicua import capicua
from iguals import igual1n
from iguals import iguals12pu
from llegir_vectors import llegir_vector
from maxim import maxim
from ordenar import ordenat
from ordenar import ordenar
from suma import suma
from suma_vectors import suma_vectors



def capcalera():
        print("*******************************************")
        print("*******************************************")
        print("*Programa per fer operacions amb vectors")
        print("*")

def menu():
        print("\n")
        print("Les opcions desponibles son:\n")
        print("    1. Es capicua?\n")
        print("    2. Calcul del maxim d'un vector\n")
        print("    3. Ordenar els vectors?\n")
        print("    4. Està ordenat?\n")
        print("    5. Calcul de la suma dels elements d'un vector\n")
        print("    6. Sumar dos vectors\n")
        print("    7. Sortir\n")
        print("\n")
        print("Entreu la vostra opcion:")
        o = int(input())
        return o

def vectors():
        capcalera()
        opcio = menu()
        while opcio != 7:
                if opcio == 2:
                    vector = llegir_vector()
                    r = maxim(vector)
                elif opcio == 5:
                    vector = llegir_vector()
                    r = suma(vector)        
                elif opcio == 1:
                    vector = llegir_vector()
                    r = capicua(vector)
                elif opcio == 3:
                    vector = llegir_vector()
                    r = ordenat(vector)
                elif opcio == 4:
                    vector = llegir_vector()
                    r = ordenar(vector)
                elif opcio == 6:
                    vector = llegir_vector()
                    r = suma_vectors()
                print(r)
                opcio = menu()
        print("adeu")



def main():
	vectors()
'''	
	vector = llegir_vector()
	print(vector)
	ord=ordenar(vector)
	print(str(ord))

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
