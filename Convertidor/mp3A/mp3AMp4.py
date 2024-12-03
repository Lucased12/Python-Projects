import os
import subprocess
from tkinter import messagebox

def convertirMp3AMp4(archivoEntrada):
   
    if not archivoEntrada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")
        return

    archivoSalida = os.path.splitext(archivoEntrada)[0] + ".mp4"
    imagenFondo = "background.jpg"  #se puede cambiar la imagen pero tiene que ser nombrado como backgroung.jpg mas que nada porque esta nonbrado asi en todo el codigo

    if not os.path.exists(imagenFondo):
        messagebox.showerror("Error", f"No se encontró la imagen de fondo: {imagenFondo}")
        return

    comando = [
        "ffmpeg",
        "-loop", "1",            #repetir la imagen
        "-i", imagenFondo,       #imagen
        "-i", archivoEntrada,    #archivio
        "-c:v", "libx264",       #codec de video (revisar porque no estoy seguro de si es la mas eficiente)
        "-c:a", "aac",           #codec de audio (lo mismo de antes)
        "-shortest",             #cambiar la duración del video al audio
        archivoSalida
    ]

    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        messagebox.showinfo("Éxito", f"Conversión a MP4 completa: {archivoSalida}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un problema durante la conversión a MP4: {e}\n{e.stderr}")
