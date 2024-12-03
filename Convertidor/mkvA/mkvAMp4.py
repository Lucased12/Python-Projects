import moviepy.editor as mp
import os

def convertirMkvAMp4(rutaArchivoEntrada):
    """Convierte un archivo MKV a MP4."""
    if not rutaArchivoEntrada.lower().endswith('.mkv'):
        raise ValueError("El archivo debe ser de tipo MKV")

    #salida del archivo
    rutaArchivoSalida = os.path.splitext(rutaArchivoEntrada)[0] + '.mp4'

    video = mp.VideoFileClip(rutaArchivoEntrada)

    video.write_videofile(rutaArchivoSalida, codec='libx264')

    video.close()

    print(f"Conversión completada: {rutaArchivoSalida}")
