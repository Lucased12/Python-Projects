import moviepy.editor as mp
import os

def convertirMkvAMp3(rutaArchivoEntrada):
    """Convierte un archivo MKV a MP3 extrayendo el audio."""
    if not rutaArchivoEntrada.lower().endswith('.mkv'):
        raise ValueError("El archivo debe ser de tipo MKV")

    rutaArchivoSalida = os.path.splitext(rutaArchivoEntrada)[0] + '.mp3'

    video = mp.VideoFileClip(rutaArchivoEntrada)

    #extrae y covierte audio
    audio = video.audio
    audio.write_audiofile(rutaArchivoSalida)

    #cerrar los objetos de audio y video
    audio.close()
    video.close()

    print(f"Conversión completada: {rutaArchivoSalida}")
