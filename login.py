from tkinter import Tk, Label, Button, Entry, messagebox
import subprocess
import psycopg2

def open_register():
    ventana.destroy()  # Cierra la ventana actual
    subprocess.call(["python", "register.py"])  # Abre el archivo de registro

def open_home():
    ventana.destroy()  # Cierra la ventana actual
    subprocess.call(["python", "home.py"])  # Abre el archivo de inicio

# Funciones para manejar el placeholder
def on_entry_click_usuario(event):
    if entry_usuario.get() == 'Correo':
        entry_usuario.delete(0, "end")  # Borrar el contenido del Entry cuando se hace clic
        entry_usuario.config(fg='black')

def on_focusout_usuario(event):
    if entry_usuario.get() == '':
        entry_usuario.insert(0, 'Correo')
        entry_usuario.config(fg='grey')

def on_entry_click_contrasena(event):
    if entry_contrasena.get() == 'Contraseña':
        entry_contrasena.delete(0, "end")  # Borrar el contenido del Entry cuando se hace clic
        entry_contrasena.config(show="*", fg='black')  # Mostrar asteriscos para la contraseña

def on_focusout_contrasena(event):
    if entry_contrasena.get() == '':
        entry_contrasena.insert(0, 'Contraseña')
        entry_contrasena.config(show="", fg='grey')

def verificar_credenciales(correo, contrasena):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            database='PruebaPrediccion',
            user='postgres',
            password='calero031731'
        )
        cursor = connection.cursor()
        # Ejecutar la consulta para verificar las credenciales
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s", (correo, contrasena))
        resultado = cursor.fetchone()
        cursor.close()
        connection.close()
        if resultado:
            return True
        else:
            return False
    except Exception as e:
        messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")
        return False

def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if verificar_credenciales(usuario, contrasena):
        open_home()  # Si las credenciales son válidas, abre la ventana de inicio
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = Tk()
ventana.title("LOGIN")
# Establecer el tamaño de la ventana
ancho_ventana = 500
alto_ventana = 300
# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
# Calcular la posición del centro
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
# Establecer la posición y el tamaño de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
# Evita que el tamaño de la ventana se manipualdo manualmente  
ventana.resizable(False, False)

# Crear los Labels
lbl = Label(ventana, text="Bienvenido", font=("Arial", 24))
lbl.pack()

lbl_usuario = Label(ventana, text="Usuario", font=("Arial", 10))
lbl_usuario.place(x=100, y=50)

lbl_contrasena = Label(ventana, text="Contraseña", font=("Arial", 10))
lbl_contrasena.place(x=100, y=100)

# Crear los Entrys con placeholders
entry_usuario = Entry(ventana, bg="pink")
entry_usuario.place(x=200, y=50, width=200, height=30)
entry_usuario.insert(0, 'Correo')
entry_usuario.config(fg='grey')
entry_usuario.bind('<FocusIn>', on_entry_click_usuario)
entry_usuario.bind('<FocusOut>', on_focusout_usuario)

entry_contrasena = Entry(ventana, bg="pink", show="")
entry_contrasena.place(x=200, y=100, width=200, height=30)
entry_contrasena.insert(0, 'Contraseña')
entry_contrasena.config(fg='grey')
entry_contrasena.bind('<FocusIn>', on_entry_click_contrasena)
entry_contrasena.bind('<FocusOut>', on_focusout_contrasena)

# Crear el botón para iniciar sesión
btn_iniciar_sesion = Button(ventana, text='Iniciar Sesión', command=iniciar_sesion, bg="green")
btn_iniciar_sesion.place(x=200, y=150, width=150)

# Crear el botón para abrir la ventana de registro
btn_registrarse = Button(ventana, text='Registrarse', command=open_register, bg="green")
btn_registrarse.place(x=200, y=200, width=150)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
