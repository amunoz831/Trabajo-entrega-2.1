from usuario import Usuario
class ValidarUsuario:

    def __init__(self, usuario:Usuario)-> None:
        self.correo:str=usuario.direccion 

    def validar(self)->bool:
        if "@" in self.correo and "." in self.correo:
            return True
        else:
            return False