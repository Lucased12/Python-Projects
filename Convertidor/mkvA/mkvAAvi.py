import moviepy.editor as mp
import os

def convertirMkvAAvi(rutaArchivoEntrada):
    """Convierte un archivo MKV a AVI."""
    if not rutaArchivoEntrada.lower().endswith('.mkv'):
        raise ValueError("El archivo debe ser de tipo MKV")

    rutaArchivoSalida = os.path.splitext(rutaArchivoEntrada)[0] + '.avi'

    video = mp.VideoFileClip(rutaArchivoEntrada)

    #escribir el archivo AVI
    video.write_videofile(rutaArchivoSalida, codec='png') 

    video.close()

    print(f"Conversión completada: {rutaArchivoSalida}")
