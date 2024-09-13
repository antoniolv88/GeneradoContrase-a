import random
import string

def generar_contrasena(longitud):
    # Definimos los caracteres que usaremos para generar la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generamos la contraseña eligiendo caracteres aleatorios
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

# Longitud de la contraseña que se desea generar
longitud_contrasena = int(input("Introduce la longitud de la contraseña: "))

# Generar y mostrar la contraseña
print("Tu contraseña generada es:", generar_contrasena(longitud_contrasena))
