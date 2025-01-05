import tkinter as tk
from tkinter.font import Font
import string
import random
import util.generic as utl
from tkinter import messagebox

# Crear la ventana principal de la aplicación
root = tk.Tk()

class GeneradorContraseñas:
    def __init__(self, root):
        # Inicializar la ventana principal
        self.root = root
        self.root.title('Generador de Contraseñas')
        self.root.geometry('900x500')
        self.root.configure(bg='#fcfcfc')
        self.root.resizable(width=0, height=0)
        utl.centrar_ventana(self.root,900,500) # Centrar la ventana en la pantalla
        
        # Cargar la imagen del logo
        self.logo = utl.leer_imagen("img/image.png", (200,200))
        
        # Crear el marco para el logo
        self.frame_logo = tk.Frame(self.root, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#AFB2B7")
        self.frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        
        # Crear la etiqueta para mostrar el logo
        self.label = tk.Label(self.frame_logo, image=self.logo, bg="#AFB2B7")
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Define una fuente personalizada
        self.tipografia_titulo = Font(family="Poppins", size=25, weight="bold")
        self.tipografia_subtitulo = Font(family="Poppins", size=14)
        self.tipografia_texto = Font(family="Poppins", size=12)
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------
        self.titulo = tk.Label(self.root, text='Generador de Contraseñas', font=self.tipografia_titulo, bg='#fcfcfc')
        self.titulo.pack(anchor='center', pady=10, padx=10)
        
        self.texto = tk.Label(self.root, text='Cree contraseñas seguras para proteger sus cuentas de Internet.', font=self.tipografia_texto, bg='#fcfcfc')
        self.texto.pack()
        # -------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.frame = tk.Frame(self.root, bg='#fcfcfc')
        self.frame.pack(padx=40, pady=40, fill='both', expand=True)
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------
        self.label_longitud = tk.Label(self.frame, text='Longitud de la contraseña:', bg='#fcfcfc', font=self.tipografia_subtitulo)
        self.label_longitud.pack(anchor='w', pady=10, padx=10)
        # -------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.entry_longitud = tk.Entry(self.frame)
        self.entry_longitud.pack(anchor='w',pady=5, padx=10)
        
        # Almacena el tipo de contraseña que se va a generar
        self.tipo_contraseña = tk.IntVar(value=1)
        
        # Opciones
        self.buttonCaracteres = tk.Radiobutton(self.frame, text="Todos los caracteres", variable=self.tipo_contraseña, value=1,  bg='#fcfcfc', takefocus=0)
        self.buttonCaracteres.pack(anchor='w',pady=5, padx=10)
        
        self.buttonLeer = tk.Radiobutton(self.frame, text="Facil de leer", variable=self.tipo_contraseña, value=2,  bg='#fcfcfc',takefocus=0)
        self.buttonLeer.pack(anchor='w',pady=5, padx=10)
        
        # Boton para generar la contraseña
        self.boton_generar = tk.Button(self.frame, text='Generar', command=self.generar)
        self.boton_generar.pack(anchor='w',pady=20)
        
        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(self.frame, text='', bg='#fcfcfc')
        self.label_resultado.pack(pady=5)
        
        # Boton para salir de la aplicacion
        self.boton_salir = tk.Button(self.frame, text='Salir', command=self.salir)
        self.boton_salir.pack(pady=5)
    
    # Funciones
    def generar_todos_los_caracteres(self):
        longitud = int(self.entry_longitud.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        self.label_resultado.config(text=f'La contraseña generada es: {contraseña}')
    
    def generar_facil_leer(self):
        longitud = int(self.entry_longitud.get())
        caracteres = string.ascii_letters
        contraseña =  ''.join(random.choice(caracteres) for i in range(longitud))
        self.label_resultado.config(text=f'La contraseña generada es: {contraseña}')
    
    def generar(self):
        try:
            longitud = int(self.entry_longitud.get())
            if self.tipo_contraseña.get() == 1:
                self.generar_todos_los_caracteres()
            else:
                self.generar_facil_leer()
        except:
            messagebox.showerror('Error', 'Por favor ingrese un valor valido')
    
    def salir(self):
        self.root.destroy()

# -------------------------------------------------------------------------------------------------------------------------------------------------

app = GeneradorContraseñas(root)
root.mainloop()