def entra_numero(msg):
 
    if not msg:
        msg = "Entra un numero: "
 
    while True:
        s = input(msg)
        if s.isnumeric():    
            n = int(s)        
            return n
 
        print("Es necessita un numero!")
 
 
def entra_numero_senar(msg):
 
    if not msg:
        msg = "Entra un numero senar: "
 
    while True:
        n = entra_numero(msg)
        if n%2==1:
            return n
 
        print("cal un nombre senar!")
 
 
