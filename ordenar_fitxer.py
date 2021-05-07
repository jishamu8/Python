def ordenacio_fitxers():
    r = llegir_fitxer("r")
    w = llegir_fitxer("w")
    v = ordenar(r)
    escriure(w,v)
 
def escriure(fo,vector_de_linies):
    n = len(vector_de_linies)
    for i in range(n):
        fo.write(vector_de_linies[i])
 
    fo.close()
 
def llegir_fitxer(mode):
    if (mode == "r"):
        pregunta = "Entra el nom de l'arxiu a llegir: "
    else:
        pregunta = "Entra el nom de l'arxiu a escriure: "
 
    nom = input(pregunta)
    f = open(nom,mode)
    return f
 
def canviar_linies(v,i,j):
    espai_auxiliar = v[i]
    v[i] = v[j]
    v[j] = espai_auxiliar
 
 
 
# fi (fitxer input), fo (fitxer output) son dor arxius oberts
def ordenar(fi):
    vector = fi.readlines()
    n = len(vector)
    for i in range(n):
        for j in range(n):
            # en aquest espai ja tenim totes les parelles possibles
            # nomes ens interessen la meitat (menos inclús)
            # PERQUE comparar la primera linia i la segona es lo mateix que comparar la segona amb la primera
            # i tampoc ens interessa comparar la primera amb la primera
 
            if (j>i):
                if (vector[j] < vector[i]):
                    canviar_linies(vector,i,j)
 
 
    fi.close()
    return vector
 
 
ordenacio_fitxers()