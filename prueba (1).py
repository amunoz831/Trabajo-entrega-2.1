bicicletas_disponibles=[]

def agregar_bicicleta(bicicleta):
    bicicletas_disponibles.append(bicicleta)

    
def agregar_bicicletas():
    bicicletas=["specialized","trek","scoot","cube","cannondale","BMC bikes","Orbea bikes","santa cruz","cervelo"]
    for id in bicicletas:
        agregar_bicicleta(id)


agregar_bicicletas()
print(bicicletas_disponibles)