def llegir_fitxer(mode):
    if (mode == "r"):
        pregunta = "Entra el nom de l'arxiu a llegir: "
    else:
        pregunta = "Entra el nom de l'arxiu a escriure: "
 
    nom = input(pregunta)
    f = open(nom,mode)
    return f
 
 
 
def fusio():
    f1 = llegir_fitxer("r")
    f2 = llegir_fitxer("r")
    f3 = llegir_fitxer("w")
    l1 = f1.readline()
    l2 = f2.readline()
    while (len(l1) > 0 and len(l2) > 0):
        if (l1 < l2):
            f3.write(l1)
            l1 = f1.readline()
        else:
            f3.write(l2)
            l2 = f2.readline()
 
    while (len(l1) > 0):
        f3.write(l1)
        l1 = f1.readline()
 
    while (len(l2) > 0):
        f3.write(l2)
        l2 = f2.readline()
 
    f1.close()
    f2.close()
    f3.close()