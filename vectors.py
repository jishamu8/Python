#imports
from capicua import capicua
from iguals import igual1n
from iguals import iguals12pu
from llegir_vectors import llegir_vector
from maxim import maxim
from ordenar import ordenat
from ordenar import ordenar
from suma import suma



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
        print("    6. Sortir\n")
        print("\n")
        print("Entreu la vostra opcion:")
        o = int(input())
        return o

def vectors():
        capcalera()
        opcio = menu()
        while opcio != 6:
                vector = llegir_vector()
                if opcio == 2:
                        m = maxim(vector)
                        print("El maxim es " + str(m))
                elif opcio == 5: 
                        s = suma(vector)
                        print("La suma es " + str(s))
                elif opcio == 1: 
                        c = capicua(vector)
                        print((c)+ " Es capicua")           
                elif opcio == 3: 
                        o = ordenat(vector)
                        print((o) + " està ordenat")
                elif opcio == 4: 
                        ord = ordenar(vector)
                        print("Vectors en orden " + str(ord))

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
