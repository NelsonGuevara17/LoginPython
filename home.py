from tkinter import Tk, Label, Button, Entry
import subprocess

def close():
    ventana.destroy()  # Cierra la ventana actual
    subprocess.call(["python", "login.py"])  # Abre el segundo archivo

ventana = Tk()
ventana.title("HOME")

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Establecer la geometría de la ventana para ocupar toda la pantalla
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

# Crear un Label en la ventana
lbl = Label(ventana, text="¡Bienvenido a mi aplicación al 100% de pantalla!", font=("Arial", 24))
lbl.pack(pady=50, padx=50)  # Añadir márgenes interiores al Label

btn_open_second = Button(ventana, text='Cerrar Cuenta', command=close, bg="green")
btn_open_second.place(x=200, y=200, width=150)

lbl.pack()

ventana.mainloop()