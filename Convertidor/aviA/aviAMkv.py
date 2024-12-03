import os
from moviepy.editor import VideoFileClip
from tkinter import messagebox

def convertirAviAMkv(archivo_entrada):
    if not archivo_entrada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")
        return

    archivo_salida = os.path.splitext(archivo_entrada)[0] + ".mkv"
    try:
        video = VideoFileClip(archivo_entrada)
        video.write_videofile(archivo_salida, codec='libx264')
        messagebox.showinfo("Éxito", f"Conversión a MKV completa: {archivo_salida}")
    except Exception as error:
        messagebox.showerror("Error", f"Hubo un problema durante la conversión a MKV: {error}")
