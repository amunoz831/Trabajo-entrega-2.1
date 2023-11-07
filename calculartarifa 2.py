import datetime as dt
from bicicleta import Bicicleta

class CalcularTarifa:

    def __init__(self,bicicleta:Bicicleta):

        self.tiempo:int=int(bicicleta.tiempo_de_llegada.minute-bicicleta.tiempo_de_salida.minute)
  
    def tarifa(self)->int:
        tiempogratis=dt.timedelta(minutes=30)
        if self.tiempo < tiempogratis:
             return 0
        else:
            total=(self.tiempo/60)*20
            return total