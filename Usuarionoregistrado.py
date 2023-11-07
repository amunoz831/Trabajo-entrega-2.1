from usuario import Usuario
from UsuarioError import UsuarioError

class UsuarioNoRegistradoError(UsuarioError):

    def __init__(self, usuario: Usuario):
        super().__init__(usuario)

    def __str__(self) -> str:
        return f"El usuario con nombre {self.usuario.direccion} no ha sido registrado"