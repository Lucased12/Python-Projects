import subprocess
import os

def convertirMp3AAvi(archivoEntrada):
    archivoSalida = os.path.splitext(archivoEntrada)[0] + ".avi"
    comando = [
        "ffmpeg",
        "-loop", "1",
        "-i", "background.jpg",
        "-i", archivoEntrada,
        "-c:v", "libx264",
        "-c:a", "mp3", 
        "-shortest",
        archivoSalida
    ]
    subprocess.run(comando)
