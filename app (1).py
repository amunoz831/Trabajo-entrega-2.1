import tkinter as tk
from tkinter import messagebox
from estacion import Estacion
from BicicletaNoEncontradaerror import BicicletaNoEncontradaError
from Usuarionoregistrado import UsuarioNoRegistradoError

class AplicacionTkinter:
    def __init__(self, ventana):
        self.estacion = Estacion()
        self.ventana = ventana
        self.ventana.title("Sistema de Alquiler de Bicicletas")
        self.estacion.agregar_bicicletas()

        # Crear etiquetas y entradas para el registro de usuarios
        self.etiqueta_nombre = tk.Label(ventana, text="Nombre:")
        self.etiqueta_telefono = tk.Label(ventana, text="Teléfono:")
        self.etiqueta_direccion = tk.Label(ventana, text="Dirección:")
        self.nombre = tk.Entry(ventana)
        self.telefono = tk.Entry(ventana)
        self.direccion = tk.Entry(ventana)

        # Crear botón para registrar usuarios
        self.boton_registrar = tk.Button(ventana, text="Registrar Usuario", command=self.registrar_usuario)

        # Crear etiquetas y entradas para alquilar bicicletas
        self.etiqueta_usuario = tk.Label(ventana, text="Usuario:")
        self.etiqueta_bicicleta = tk.Label(ventana, text="ID de Bicicleta:")
        self.usuario = tk.Entry(ventana)
        self.bicicleta = tk.Entry(ventana)

        # Crear botón para alquilar bicicletas
        self.boton_alquilar = tk.Button(ventana, text="Alquilar Bicicleta", command=self.alquilar_bicicleta)

        # Crear etiquetas y entradas para recibir bicicletas
        self.etiqueta_usuario_devolver = tk.Label(ventana, text="Usuario:")
        self.etiqueta_bicicleta_devolver = tk.Label(ventana, text="ID de Bicicleta:")
        self.usuario_devolver = tk.Entry(ventana)
        self.bicicleta_devolver = tk.Entry(ventana)

        # Crear botón para recibir bicicletas
        self.boton_recibir = tk.Button(ventana, text="Recibir Bicicleta", command=self.recibir_bicicleta)

        # Crear etiqueta y entrada para consultar disponibilidad
        self.etiqueta_consulta_id = tk.Label(ventana, text="ID de Bicicleta a Consultar:")
        self.id_consulta = tk.Entry(ventana)

        # Crear botón para consultar disponibilidad
        self.boton_consultar_disponibilidad = tk.Button(ventana, text="Consultar Disponibilidad", command=self.consultar_disponibilidad)

        # Colocar los elementos en la ventana
        self.etiqueta_nombre.grid(row=0, column=0)
        self.etiqueta_telefono.grid(row=0, column=2)
        self.etiqueta_direccion.grid(row=0, column=4)
        self.nombre.grid(row=1, column=0)
        self.telefono.grid(row=1, column=2)
        self.direccion.grid(row=1, column=4)
        self.boton_registrar.grid(row=1, column=6)

        self.etiqueta_usuario.grid(row=2, column=0)
        self.etiqueta_bicicleta.grid(row=2, column=2)
        self.usuario.grid(row=3, column=0)
        self.bicicleta.grid(row=3, column=2)
        self.boton_alquilar.grid(row=3, column=6)

        self.etiqueta_usuario_devolver.grid(row=4, column=0)
        self.etiqueta_bicicleta_devolver.grid(row=4, column=2)
        self.usuario_devolver.grid(row=5, column=0)
        self.bicicleta_devolver.grid(row=5, column=2)
        self.boton_recibir.grid(row=5, column=6)

        self.etiqueta_consulta_id.grid(row=6, column=0)
        self.id_consulta.grid(row=7, column=0)
        self.boton_consultar_disponibilidad.grid(row=7, column=6)

    def registrar_usuario(self):
        nombre = self.nombre.get()
        telefono = int(self.telefono.get())
        direccion = self.direccion.get()
        try:
            self.estacion.registrar_usuario(nombre, telefono, direccion)
            tk.messagebox.showinfo("Registro Exitoso", f"El usuario {nombre} ha sido registrado exitosamente.")
        except UsuarioNoRegistradoError as e:
            tk.messagebox.showerror("Error de Registro", f"Error: {e}")

    def alquilar_bicicleta(self):
        usuario = self.usuario.get()
        bicicleta_id = self.bicicleta.get()
        try:
            resultado = self.estacion.alquilar_bicicleta_a_cliente(bicicleta_id, usuario)
            tk.messagebox.showinfo("Alquiler Exitoso", resultado)
        except BicicletaNoEncontradaError as e:
            tk.messagebox.showerror("Error de Alquiler", f"Error: {e}")

    def recibir_bicicleta(self):
        usuario = self.usuario_devolver.get()
        bicicleta_id = self.bicicleta_devolver.get()
        try:
            
            resultado = self.estacion.recibir_bicicleta(bicicleta_id, usuario)
            tk.messagebox.showinfo("Recepción Exitosa", resultado)
        except BicicletaNoEncontradaError as e:
             tk.messagebox.showerror("Error al Recibir", f"Error: {e}")



    def consultar_disponibilidad(self):
        id_bicicleta = self.id_consulta.get()
        resultado = self.estacion.consultar_disponibilidad(id_bicicleta)
        tk.messagebox.showinfo("Consulta de Disponibilidad", resultado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionTkinter(ventana)
    ventana.mainloop()

 
