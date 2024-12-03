import subprocess
import os

def convertirMp3AMkv(archivoEntrada):
    archivoSalida = os.path.splitext(archivoEntrada)[0] + ".mkv"
    comando = [
        "ffmpeg",
        "-loop", "1",
        "-i", "background.jpg",
        "-i", archivoEntrada,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        archivoSalida
    ]
    subprocess.run(comando)

                #revisar mp3 a mp4 que tiene los comentarios