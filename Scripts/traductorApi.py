# Github: https://github.com/Lucased12

from tkinter import Tk, Label, Entry, Button
from googletrans import Translator
from PIL import Image, ImageTk

#Traducir el texto ingresado
def traducirTexto():
    #Obtener el texto ingresado por el usuario
    textoEntrada = entradaTexto.get()

    #Traducir el texto
    traductor = Translator()
    textoTraducido = traductor.translate(textoEntrada, dest='en').text

    #Mostrar la traducción en la etiqueta
    etiquetaSalida.config(text="Traducción: " + textoTraducido)

#Funcion para cerrar la aplicación
def cerrarApp():
    raiz.destroy()

#Configuracion de la interfaz gráfica
raiz = Tk()
raiz.title("Traductor")

#Colores
raiz.configure(bg='#2c3e50')
colorTexto = '#ecf0f1'

#Etiqueta y entrada para el texto que se va a traducir
etiquetaEntrada = Label(raiz, text="Texto a Traducir:", bg='#2c3e50', fg=colorTexto)
etiquetaEntrada.pack()
entradaTexto = Entry(raiz, width=50)
entradaTexto.pack()

#Boton para iniciar la traducción
botonTraducir = Button(raiz, text="Traducir", command=traducirTexto, bg='#34495e', fg=colorTexto)
botonTraducir.pack(side='left')

#Etiqueta para mostrar la traducción
etiquetaSalida = Label(raiz, text="", bg='#2c3e50', fg=colorTexto)
etiquetaSalida.pack()

raiz.mainloop()
