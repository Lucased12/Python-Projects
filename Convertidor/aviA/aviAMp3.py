import os
from moviepy.editor import VideoFileClip
from tkinter import messagebox

def convertirAviAMp3(archivoEntrada):
    if not archivoEntrada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")
        return

    archivoSalida = os.path.splitext(archivoEntrada)[0] + ".mp3"
    try:
        video = VideoFileClip(archivoEntrada)
        video.audio.write_audiofile(archivoSalida)
        messagebox.showinfo("Éxito", f"Conversión a MP3 completa: {archivoSalida}")
    except Exception as error:
        messagebox.showerror("Error", f"Hubo un problema durante la conversión a MP3: {error}")
