import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

class Monitor:
    def __init__(self, nombre, codigo_estudiante, evento_asignado):
        self.__nombre = nombre
        self.__codigo_estudiante = codigo_estudiante
        self.__evento_asignado = evento_asignado
        self.__horas_acumuladas = 0.0

    def get_nombre(self):
        return self.__nombre

    def get_codigo_estudiante(self):
        return self.__codigo_estudiante

    def get_evento_asignado(self):
        return self.__evento_asignado

    def get_horas_acumuladas(self):
        return self.__horas_acumuladas

    def registrar_horas(self, horas):
        self.__horas_acumuladas += horas

    def verificar_estado(self):
        if self.__horas_acumuladas >= 8:
            return "✅ Horas completadas"
        else:
            return "⏳ Horas pendientes"

def mostrar_info(m):
    return f"👤 {m.get_nombre()}\n📌 {m.get_evento_asignado()}\n" \
           f"⏱ {m.get_horas_acumuladas()} horas\n📈 {m.verificar_estado()}\n\n"

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Crear 5 monitores con datos fijos
    m1 = Monitor("Ana Pérez", "101", "Feria Universitaria")
    m2 = Monitor("Carlos Rojas", "102", "Colegio San Luis")
    m3 = Monitor("Laura Gómez", "103", "Open House")
    m4 = Monitor("Mateo Díaz", "104", "ExpoUniversidades")
    m5 = Monitor("Valentina Ruiz", "105", "Semana Juventud")

    while True:
        opcion = simpledialog.askstring("📋 MENÚ",
            "1. Registrar Horas\n2. Ver Estado\n3. Salir")

        if opcion is None:
            continue

        if opcion == "1":
            sel = simpledialog.askstring("Seleccionar Monitor",
                "1. Ana\n2. Carlos\n3. Laura\n4. Mateo\n5. Valentina")

            monitor = {
                "1": m1, "2": m2, "3": m3, "4": m4, "5": m5
            }.get(sel)

            if monitor is None:
                messagebox.showerror("Error", "Selección inválida.")
                continue

            try:
                horas_str = simpledialog.askstring("Registrar Horas", "¿Cuántas horas desea registrar?")
                if horas_str is None:
                    continue
                horas = float(horas_str)
                if horas <= 0:
                    raise ValueError
                monitor.registrar_horas(horas)
                messagebox.showinfo("Registro Exitoso",
                    f"✅ {monitor.get_nombre()}: {monitor.get_horas_acumuladas()} horas.")
            except ValueError:
                messagebox.showerror("Error", "Número inválido.")

        elif opcion == "2":
            resumen = ""
            for m in [m1, m2, m3, m4, m5]:
                resumen += mostrar_info(m)
            area = scrolledtext.ScrolledText(width=50, height=15)
            area.insert(tk.END, resumen)
            area.configure(state='disabled')
            top = tk.Toplevel()
            top.title("Resumen de Monitores")
            area.pack()
        elif opcion == "3":
            messagebox.showinfo("Salir", "👋 ¡Hasta pronto!")
            break
        else:
            messagebox.showwarning("Opción inválida", "Por favor elige una opción válida.")

if __name__ == "__main__":
    main()
