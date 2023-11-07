from bicicleta import Bicicleta

    
class BicicletaNoEncontradaError(Exception):
    def __init__(self, bicicleta:Bicicleta):
        self.id=bicicleta.id

    def __str__(self) -> str:
        return f"No se encontró la bicicleta con el ID '{self.id}'."