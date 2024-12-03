import os
from moviepy.editor import VideoFileClip
from tkinter import messagebox

def convertir_mp4_a_mp3(archivoEntrada):
    if not archivoEntrada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")
        return

    archivoSalida = os.path.splitext(archivoEntrada)[0] + ".mp3"
    try:
        video = VideoFileClip(archivoEntrada)
        video.audio.write_audiofile(archivoSalida)
        messagebox.showinfo("Éxito", f"Conversión a MP3 completa: {archivoSalida}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema durante la conversión a MP3: {e}")

        
#moviepy para extraer el audio