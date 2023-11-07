import datetime as dt 
from usuario import Usuario

class Bicicleta:
    def __init__(self, id:str):#el id en este caso seria el modelo de la bicicleta pero decidimos llamarlo id
        self.id:str = id
        self.disponible:bool = True

    def alquilar(self)->bool:
        if self.disponible:
            self.disponible = False    
            return True
        else:
            return False

    def devolver(self)->bool:
        if not self.disponible:
            self.disponible = True
            return True
        else:
            return False
        
    def registrar_alquiler(self,usuario:Usuario):
        duracion=self.tiempo_de_llegada-self.tiempo_de_salida
        duracion_precio=((duracion/60)*20)
        usuario.alquileres.append((duracion,duracion_precio))
        



