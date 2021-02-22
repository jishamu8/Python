def menu():
    print ("1. Pintar quadrat")
    print ("2. Pintar un triangle")
    print ("3. Pintar un triangle invers")
    print ("0. Sortir")
    print
    opcio = input("Introdueix opcio: ")
    while opcio not in range(3):
        opcio = raw_input("opcio no permesa. Reintrodueix opcio: ")
    return opcio

def pintar_quadrat():
	print ("Quina dimencio vol ")
	n =int(input())
	for i in range(n):
		for j in range(n):
			print ("*", end="")
		print()

def triangle():
    print ("Quina dimencio vol ")
    n =int(input())
    for i in range(n):
        for j in range(i+1):
            print ("*", end="")
        print()

def triangle_invers():
    print ("Quina dimencio vol ")
    n =int(input())
    for i in range(n):
        for j in range(n-i):
            print ("*", end="")
        print()


def main():
	print ("=========")
	print ("GEOMETRIA")
	print ("=========")
	print ()
	end = False
	while not end:
    	op = menu()
    	if op == 1:
        	triangle()
    	elif op == 2:
        	triangle_invers()
    	else:
        	end = True
main()
