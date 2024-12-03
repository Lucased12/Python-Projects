# Github: https://github.com/Lucased12

from tkinter import Label, Frame, Button, Canvas

class disenioConvertidorVideo:
    def __init__(self, ventana):
        self.ventana = ventana

    def configurarDisenio(self, archivoEntrada, callbackSoltado, callbacksConversion):
        """Configura el diseño de la interfaz gráfica."""
        self.ventana.title("Conversor de Formatos")
        self.ventana.geometry("600x300")
        self.ventana.resizable(False, False)

        #marco
        lienzo = Canvas(self.ventana, width=600, height=300, bg="#1A1A1D")  #codigo hexadecimal ok 
        lienzo.pack(fill="both", expand=True)

        marcoTitulo = Frame(lienzo, bg="#1A1A1D")  #color de fondo ok
        marcoTitulo.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)

        etiquetaTitulo = Label(marcoTitulo, text="Convertidor de formatos", fg="white", font=("Roboto", 20, "bold"), bg="#1A1A1D") 
        etiquetaTitulo.pack(anchor="center")

        marcoArrastre = Frame(lienzo, bg="#ECDFCC", highlightbackground="black", highlightthickness=2)  
        marcoArrastre.place(relx=0.05, rely=0.3, relwidth=0.6, relheight=0.6)

        etiquetaArrastre = Label(marcoArrastre, text="Arrastre el archivo a convertir!", fg="black", font=("Roboto", 12, "bold"), bg="#ECDFCC")  
        etiquetaArrastre.pack(pady=10)

        self.etiquetaArchivo = Label(marcoArrastre, text="No se ha detectado ningún archivo", fg="black", font=("Roboto", 10), bg="#ECDFCC")  
        self.etiquetaArchivo.pack(pady=5)

        marcoBotones = Frame(lienzo, bg="#697565")  
        marcoBotones.place(relx=0.7, rely=0.3, relwidth=0.25, relheight=0.6)

        self.botones = {
            'mp4': Button(marcoBotones, bg="#ECDFCC", text="Mp4", font=("Roboto", 12), command=callbacksConversion['mp4']),
            'avi': Button(marcoBotones, bg="#ECDFCC", text="Avi", font=("Arial", 12), command=callbacksConversion['avi']),
            'mkv': Button(marcoBotones, bg="#ECDFCC", text="Mkv", font=("Arial", 12), command=callbacksConversion['mkv']),
            'mp3': Button(marcoBotones, bg="#ECDFCC", text="Mp3", font=("Arial", 12), command=callbacksConversion['mp3']),
        }

        for indice, boton in enumerate(self.botones.values()):
            boton.pack(pady=5, fill="x")

        #configuracion de agarrar y soltar
        self.ventana.drop_target_register('DND_Files')
        self.ventana.dnd_bind('<<Drop>>', callbackSoltado)

    def actualizarEtiquetaArchivo(self, rutaArchivo):
        self.etiquetaArchivo.config(text=f"Archivo seleccionado: {rutaArchivo}")

    def actualizarVisibilidadBotones(self, extensionArchivo):
        """Actualiza la visibilidad de los botones de acuerdo al tipo de archivo."""
        for ext, boton in self.botones.items():
            if f'.{ext}' == extensionArchivo:
                boton.pack_forget()
            else:
                boton.pack(pady=5, fill="x")
