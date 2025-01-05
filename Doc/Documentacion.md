# Contraseñas Seguras 🔐

 Contraseñas seguras: es un proyecto desarrollado para generar y gestionar contraseñas seguras de manera eficiente, ayudando a los usuarios a proteger su información personal y profesional.

## 🚀 Características

- Generación de contraseñas seguras con parámetros personalizables.
- Interfaz sencilla y amigable

##  💁‍♀️ Guía del usuario

Contraseñas Seguras es una herramienta que permite a los usuarios generar contraseñas robustas y evaluar la seguridad de contraseñas existentes. Diseñada para usuarios que desean mejorar la seguridad de sus cuentas en línea, Contraseñas Seguras ayuda a proteger información sensible con contraseñas únicas y personalizadas.

### 🧩 Objetivos principales:
- Ayudar a los usuarios a crear contraseñas seguras.
- Proveer una interfaz simple para evaluar la fortaleza de contraseñas actuales.
- Reducir riesgos de vulnerabilidad en cuentas personales o profesionales.

## 🛠️ Instalación

1. Clona el repositorio: ```bash git clone https://github.com/MayraMoy/claves_Seguras.git cd claves_Seguras
2. Instala las dependencias: pip install -r requirements.txt
3. Ejecuta la aplicacion: python main.py

## 📖 Uso

1. Ejecuta la aplicación y selecciona las opciones deseadas para generar evaluar o contraseñas.
2. Sigue las instrucciones en la interfaz para personalizar las contraseñas según tus necesidades (por ejemplo, longitud, caracteres especiales, números, etc.).

## 🔍 Usa las funciones principales

Generar una contraseña segura : La aplicación generará una contraseña robusta y la mostrará en pantalla.

1. Elige la longitud de la contraseña.

2. Selecciona los tipos de caracteres a incluir:   
    - Todos los caracteres: incluye mayusculas, minisculas, simbolos, numeros.
    - Facil de decir: incluye letras.

## 📖 Guía para desarrolladores

Estructura del proyecto:
- main.py: archivo principal del proyecto.
- generador_claves.py : archivo que contiene la funcion para generar claves.
- index.py: contiene la interfaz de usuario.
- generic.py: contiene las configuraciones que seguirán las imágenes.  

Carpetas:
- img: contiene las imagenes utilizadas en el proyecto.
- src: contiene los archivos del codigo fuente
- util: contiene funciones auxiliares.

## 💡 Dependencias 

- Tkinter: para la interfaz de usuario.
- random: para generar contraseñas aleatorias.
- string: para trabajar con cadenas de texto.
- Font: para personalizar la fuente de la interfaz.

## ⚙️ Explicación del código

El codigo esta dividido en tres archivos principales:
- main.py: contiene la funcion principal que ejecuta la aplicacion.
- generador_claves.py: contiene la script que genera las claves.
- index.py: contiene la interfaz de usuario.

El archivo main.py:
- Importa las dependencias necesarias.

El archivo generador_claves.py:
- Contiene un script funcional para generar claves.

Por ejemplo 

```python
    def generar_contraseña(self): 
        longitud = int(self.entry_longitud.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        self.label_resultado.config(text=f'La contraseña generada es: {contraseña}')
```

El archivo index.py:
- Crea una ventana con Tkinter.
- Crea un entry para ingresar la longitud de la contraseña.
- Crea radioButton para selecionar el tipo de contraseña.
- Crea un boton para generar la contraseña.
- Crea un label para mostrar la contraseña generada.
- Crea un boton para salir de la ventana.

La clase GeneradorContraseñas es quien contiene toda la interfaz del usuario y quien maneja los script para generar las contraseñas personalizadas.

## Atributos

- **root**: (tk.Tk): La ventana principal de la aplicación. 
- **logo**: (tk.PhotoImage): La imagen del logo. 
- **frame_logo**: (tk.Frame): El marco que contiene el logo. 
- **label**: (tk.Label): La etiqueta que muestra el logo. 
- **tipografia_titulo**: (tk.Font): La fuente utilizada para los títulos. 
- **tipografia_subtitulo**: (tk.Font): La fuente utilizada para los subtítulos. 
- **tipografia_texto**: (tk.Font): La fuente utilizada para los textos. 
- **entry_longitud**: (tk.Entry): El campo de texto donde se ingresa la longitud de la contraseña.
- **tipo_contraseña**: (tk.StringVar): La variable que almacena el tipo de contraseña seleccionado.
- **buttonCaracteres**: (tk.Radiobutton): El boton para seleccionar el tipo de contraseña.
- **buttonLeer**: (tk.Radiobutton): El boton para seleccionar el tipo de contraseña.
- **boton_generar**: (tk.Button): El boton para generar la contraseña.
- **label_resultado**: (tk.Label): La etiqueta que muestra el resultado de la generacion de la contraseña.
- **boton_salir**: (tk.Button): El boton para salir.

Funciones:
- **__init__()**: Inicializa la clase y crea la interfaz de usuario.
- **generar_todos_los_caracteres()**: Genera una contraseña con todos los caracteres.
- **generar_facil_leer()**: Genera una contraseña facil de leer.
- **generar()**: Genera una contraseña segun el tipo seleccionado.
- **salir()**: Cierra la ventana.
