# Github: https://github.com/Lucased12

import random
import string

def generarContrasenia(cantidadCaracteres):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenia = ''.join(random.choice(caracteres) for _ in range(cantidadCaracteres))
    return contrasenia

def main():
    try:
        longitudMaxima = int(input("Ingresa el numero de caracteres maximos para la contrasenia: "))
        if longitudMaxima <= 0:
            print("Poner un numero positivo. >:/")
            return
        contraseniaGenerada = generarContrasenia(longitudMaxima)
        print("Contrasenia generada:", contraseniaGenerada)
    except ValueError:
        print("Hubo un error, intentar nuevamente!")

if __name__ == "__main__":
    main()
