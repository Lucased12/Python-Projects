# Github: https://github.com/Lucased12
import random

def lanzarDado():
    #Simular el lanzamiento del dado
    return random.randint(1, 6)

def main():
    print("Hola, este es un simulador de dados!")
    while True:
        input("Presiona Enter para lanzar el dado: ")
        resultado = lanzarDado()
        print("El dado a hizo lanzado, toco: ", resultado)
        jugar_de_nuevo = input("Queres lanzar el dado de nuevo? (si/no): ")
        if jugar_de_nuevo.lower() != 'si':
            print("Gracias por usar este scipt!")
            break

if __name__ == "__main__":
    main()