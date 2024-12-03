import os
import moviepy.editor as mp

def convertirAviAMp4(rutaArchivoEntrada):
    """Convierte un archivo AVI a MP4."""
    if not rutaArchivoEntrada.lower().endswith('.avi'):
        raise ValueError("El archivo debe ser de tipo AVI")

    rutaArchivoSalida = os.path.splitext(rutaArchivoEntrada)[0] + '.mp4'

    #cargar el archivito Aiv
    video = mp.VideoFileClip(rutaArchivoEntrada)

    video.write_videofile(rutaArchivoSalida, codec='libx264')
    video.close()

    print(f"Conversión completada: {rutaArchivoSalida}")
