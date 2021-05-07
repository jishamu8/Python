def mayuscula():
    nom_archivo_in=input("Dime el archivo de entrada: ")
    nom_archivo_out=input("Dime el archivo de salida: ")
    archivo_in = open(nom_archivo_in,"r")
    archivo_out = open(nom_archivo_out,"w")
    vector = archivo_in.readline()
    n = len(vector)
    for i in range(n):
        lineout = vector[i].upper()
        archivo_out.write(lineout)

    archivo_in.close()
    archivo_out.close()    


mayuscula()
