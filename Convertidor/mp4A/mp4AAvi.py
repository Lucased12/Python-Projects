import os
from moviepy.editor import VideoFileClip
from tkinter import messagebox

def convertir_mp4_a_avi(archivoEntrada):
    if not archivoEntrada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")
        return

    archivoSalida = os.path.splitext(archivoEntrada)[0] + ".avi"
    try:
        video = VideoFileClip(archivoEntrada)
        video.write_videofile(archivoSalida, codec='libx264')
        messagebox.showinfo("Éxito", f"Conversión a AVI completa: {archivoSalida}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema durante la conversión a AVI: {e}")
