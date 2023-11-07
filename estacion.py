from bicicleta import Bicicleta
from usuario import Usuario
from validarusuario import ValidarUsuario
from UsusariExistenteError import UsuarioExistenteError
from Usuarionoregistrado import UsuarioNoRegistradoError
from BicicletaNoEncontradaerror import BicicletaNoEncontradaError
import datetime as dt
class Estacion:
    
    def __init__(self)->None:
        self.bicicletas_disponibles:list[Bicicleta.id] = []
        self.usuarios_registrar:dict[Usuario]={}
        self.alquileres:dict={}

    def registrar(self,usuario:Usuario):
        UsuarioValido=ValidarUsuario(usuario)
        if UsuarioValido.validar():
            self.usuarios_registrar[usuario.nombre]=usuario.direccion
            return print(f"el registro de {usuario.nombre} fue exitoso")
        else:
            raise UsuarioNoRegistradoError(usuario)

    def agregar_bicicleta(self, bicicleta:Bicicleta):
        self.bicicletas_disponibles.append(bicicleta.id)

    
    def agregar_bicicletas(self):
        self.bicicletas=["specialized","trek","scoot","cube","cannondale","BMC bikes","Orbea bikes","santa cruz","cervelo"]
        for id in self.bicicletas:
            bicicleta=Bicicleta(id)
            self.agregar_bicicleta(bicicleta)
        
        
    def __str__(self)->str:
        return f"Estación con Bicicletas disponibles: {', '.join(map(str, self.bicicletas_disponibles))}"
    
    def calcular_duracion_alquiler(self, fecha_inicio, fecha_fin):
        diferencia_fecha = fecha_fin - fecha_inicio
        segundos = diferencia_fecha.total_seconds()
        minutos = segundos // 60
        return minutos
    
    def registrar_usuario(self,nombre:str,telefono:int,direccion:str):
        if nombre not in self.usuarios_registrar.keys():
            usuario=Usuario(nombre,direccion,telefono)
            self.registrar(usuario)
        else:
            raise UsuarioExistenteError(Usuario(nombre,direccion,telefono))

    
    def alquilar_bicicleta_a_cliente(self,bicicleta,usuario:str):
        bicicleta1=Bicicleta(bicicleta)
        self.fechasalida=dt.datetime.now()
        if bicicleta in self.bicicletas_disponibles:
            if usuario in self.usuarios_registrar.keys():
                if bicicleta1.alquilar():
                    self.bicicletas_disponibles.remove(bicicleta1.id)
                    return  f"alquiler exitoso"
        else:
            raise BicicletaNoEncontradaError(bicicleta1)
        
    def tarifa(self,int)->int:
        self.tiempo=int
        tiempogratis=0
        if self.tiempo < tiempogratis:
             return print(f"el servicio es gratis")
        else:
            total=(self.tiempo)*20
            return print(f"el servicio es {total}")


    def recibir_bicicleta(self,bicicleta:str,usuario):
        bicicleta1=Bicicleta(bicicleta)
        bicicleta1.devolver()
        self.bicicletas_disponibles.append(bicicleta1.id)
        self.fechallegada=dt.datetime.now()
        self.duracion_alquiler=self.calcular_duracion_alquiler(self.fechasalida,self.fechallegada)
        self.precio=self.tarifa(self.duracion_alquiler)
        return f"{usuario} bicicleta recibida su tiempo ha sido {self.duracion_alquiler} y tiene un costo de {self.precio} "


    def consultar_disponibilidad(self, id:str)->str:
         if id in self.bicicletas_disponibles:
             return f"la bicicleta con id {id} se encuentra en la estacion"
         else: 
             return f"la bicicle ta con id {id} no se encuentra en la estacion"
            