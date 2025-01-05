import string
import random

def generar_contraseña(self):
    longitud = int(self.entry_longitud.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    self.label_resultado.config(text=f'La contraseña generada es: {contraseña}')