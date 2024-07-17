from tkinter import Tk, Label, Button, Entry, messagebox, StringVar
import subprocess
from Base_Datos import db  # Importa el módulo db

def return_login():
    ventana.destroy()  # Cierra la ventana actual
    subprocess.call(["python", "login.py"])  # Abre el segundo archivo

# Función para validar que solo se ingresen letras
def validate_only_letters(char):
    return char.isalpha() or char == ""

# Función para validar que solo se ingresen correos @gmail
def validate_gmail_email(text):
    return text.endswith('@gmail.com') or text == ""

# Función para validar que solo sean 9 números que comiencen con 9
def validate_celular(content):
    return content == "" or (content.isdigit() and len(content) <= 9 and content.startswith("9"))

# Función para validar que solo sean más de 8 caracteres la contraseña
def validate_contrasena(content):
    return content == "" or (content.isdigit() and len(content) >= 8)

# Función que se ejecuta al hacer clic en el botón de enviar para mostrar mensaje
def submit():
    celular = entry_celular.get()
    if len(celular) == 9 and celular.startswith("9"):
        messagebox.showinfo("Validación", "Número de celular válido")
    else:
        messagebox.showerror("Validación", "Número de celular inválido")

    contrasena = entry_contrasena.get()
    if len(celular) >= 8 :
        messagebox.showinfo("Validación", "Contraseña válida")
    else: 
        messagebox.showerror("Validación", "Contraseña inválida")


# Función para validar y registrar el usuario
def registrar_usuario_form():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    correo = entry_correo.get()
    celular = entry_celular.get()
    contrasena = entry_contrasena.get()
    repetir_contrasena = entry_repetir_contrasena.get()

    if not nombre:
        messagebox.showerror("Error", "El campo Nombre es obligatorio")
    elif not apellido:
        messagebox.showerror("Error", "El campo Apellido es obligatorio")
    elif not correo or not correo.endswith('@gmail.com'):
        messagebox.showerror("Error", "El campo Correo debe ser un correo electrónico Gmail válido")
    elif not celular or len(celular) != 9 or not celular.startswith("9"):
        messagebox.showerror("Error", "El campo Celular debe contener exactamente 9 dígitos y comenzar con 9")
    elif not contrasena or len(contrasena) <= 8:
        messagebox.showerror("Error", "El campo Contraseña debe contener 8 o más dígitos")
    elif not repetir_contrasena:
        messagebox.showerror("Error", "El campo Repetir Contraseña es obligatorio")
    elif contrasena != repetir_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
    else:
        db.registrar_usuario(nombre, apellido, correo, celular, contrasena)  # Llama a la función del módulo db
        messagebox.showinfo("Éxito", "Usuario registrado con éxito")
        return_login()

ventana = Tk()
ventana.title("REGISTER")

# Establecer el tamaño de la ventana
ancho_ventana = 500
alto_ventana = 500
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

lbl = Label(ventana, text="Registro", font=("Arial", 24))
lbl.pack(pady=10)

# Crear los Labels y Entrys con validación
vcmd = (ventana.register(validate_only_letters), '%S')
vcmd_gmail_email = (ventana.register(validate_gmail_email), '%P')
vcmd_celular = (ventana.register(validate_celular), '%P')

# Campo Nombre
label_nombre = Label(ventana, text="Nombre")
label_nombre.pack(pady=5)
entry_nombre = Entry(ventana, validate="key", validatecommand=vcmd)
entry_nombre.pack(pady=5)

# Campo Apellido
label_apellido = Label(ventana, text="Apellido")
label_apellido.pack(pady=5)
entry_apellido = Entry(ventana, validate="key", validatecommand=vcmd)
entry_apellido.pack(pady=5)

# Campo Correo
label_correo = Label(ventana, text="Correo Electrónico")
label_correo.pack(pady=5)
entry_correo = Entry(ventana)
entry_correo.pack(pady=5)

# Campo Celular
celular_var = StringVar()

label_celular = Label(ventana, text="Celular")
label_celular.pack(pady=5)
entry_celular = Entry(ventana, textvariable=celular_var, validate="key", validatecommand=vcmd_celular)
entry_celular.pack(pady=5)

# Campo Contraseña
label_contrasena = Label(ventana, text="Contraseña")
label_contrasena.pack(pady=5)
entry_contrasena = Entry(ventana, show='*')
entry_contrasena.pack(pady=5)

# Campo Repetir Contraseña
label_repetir_contrasena = Label(ventana, text="Repetir Contraseña")
label_repetir_contrasena.pack(pady=5)
entry_repetir_contrasena = Entry(ventana, show='*')
entry_repetir_contrasena.pack(pady=5)

# Botón de Registro
btn_registrarse = Button(ventana, text='Registrarse', command=registrar_usuario_form, bg="green")
btn_registrarse.pack(pady=20)

ventana.mainloop()
