import tkinter as tk
from tkinter import simpledialog, messagebox

class Cliente:
    def __init__(self):
        self.__nombre = ""
        self.__telefono = ""

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

class Reserva:
    def __init__(self):
        self.__numero_habitacion = 0
        self.__cantidad_noches = 0
        self.__cliente = None

    def get_numero_habitacion(self):
        return self.__numero_habitacion

    def set_numero_habitacion(self, numero):
        self.__numero_habitacion = numero

    def get_cantidad_noches(self):
        return self.__cantidad_noches

    def set_cantidad_noches(self, noches):
        self.__cantidad_noches = noches

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Crear objeto Cliente
    cliente = Cliente()

    nombre = simpledialog.askstring("Datos del Cliente", "Ingrese el nombre del cliente:")
    if nombre:
        cliente.set_nombre(nombre)
    else:
        messagebox.showerror("Error", "Nombre no ingresado")
        return

    telefono = simpledialog.askstring("Datos del Cliente", "Ingrese el teléfono del cliente:")
    if telefono:
        cliente.set_telefono(telefono)
    else:
        messagebox.showerror("Error", "Teléfono no ingresado")
        return

    # Crear objeto Reserva
    reserva = Reserva()

    try:
        habitacion_str = simpledialog.askstring("Datos de Reserva", "Ingrese el número de habitación:")
        numero_habitacion = int(habitacion_str)
        reserva.set_numero_habitacion(numero_habitacion)

        noches_str = simpledialog.askstring("Datos de Reserva", "Ingrese la cantidad de noches:")
        cantidad_noches = int(noches_str)
        reserva.set_cantidad_noches(cantidad_noches)
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Debe ingresar valores numéricos válidos.")
        return

    # Asociar cliente a la reserva
    reserva.set_cliente(cliente)

    # Mostrar resumen
    resumen = (
        "Resumen de la Reserva:\n"
        f"Cliente: {reserva.get_cliente().get_nombre()}\n"
        f"Teléfono: {reserva.get_cliente().get_telefono()}\n"
        f"Habitación: {reserva.get_numero_habitacion()}\n"
        f"Noches: {reserva.get_cantidad_noches()}"
    )

    messagebox.showinfo("Resumen de la Reserva", resumen)

if __name__ == "__main__":
    main()
