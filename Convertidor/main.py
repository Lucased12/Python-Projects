# Github: https://github.com/Lucased12

import os
from tkinterdnd2 import TkinterDnD
from disenio import disenioConvertidorVideo
from mp4A.mp4AMp3 import convertir_mp4_a_mp3
from mp4A.mp4AAvi import convertir_mp4_a_avi
from mp4A.mp4AMkv import convertir_mp4_a_mkv
from aviA.aviAMp4 import convertirAviAMp4
from aviA.aviAMkv import convertirAviAMkv
from aviA.aviAMp3 import convertirAviAMp3
from mkvA.mkvAMp3 import convertirMkvAMp3
from mkvA.mkvAMp4 import convertirMkvAMp4
from mkvA.mkvAAvi import convertirMkvAAvi
from mp3A.mp3AMp4 import convertirMp3AMp4
from mp3A.mp3AAvi import convertirMp3AAvi
from mp3A.mp3AMkv import convertirMp3AMkv

class aplicacionConvertidorVideo:
    def __init__(self, raiz):
        self.archivoEntrada = ""

        #configura la interfaz grafica usando el diseño importado
        self.disenio = disenioConvertidorVideo(raiz)
        self.disenio.configurarDisenio(
            archivoEntrada=self.archivoEntrada,
            callbackSoltado=self.en_soltar,  #asocia el evento de soltar archivos
            callbacksConversion={  #define los metodos para manejar las conversiones
                'mp3': self.convertir_a_mp3,
                'avi': self.convertir_a_avi,
                'mkv': self.convertir_a_mkv,
                'mp4': self.convertir_a_mp4,
            }
        )

    def en_soltar(self, evento):
        self.archivoEntrada = evento.data
        #identifica la extension
        extensionArchivo = os.path.splitext(self.archivoEntrada)[1].lower()

        self.disenio.actualizarEtiquetaArchivo(self.archivoEntrada)
        self.disenio.actualizarVisibilidadBotones(extensionArchivo)

    def convertir_a_mp3(self):
        if self.archivoEntrada.endswith('.mp4'):
            convertir_mp4_a_mp3(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.avi'):
            convertirAviAMp3(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.mkv'):
            convertirMkvAMp3(self.archivoEntrada)

    def convertir_a_mp4(self):
        if self.archivoEntrada.endswith('.avi'):
            convertirAviAMp4(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.mkv'):
            convertirMkvAMp4(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.mp3'):
            convertirMp3AMp4(self.archivoEntrada)

    def convertir_a_avi(self):
        if self.archivoEntrada.endswith('.mp4'):
            convertir_mp4_a_avi(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.mkv'):
            convertirMkvAAvi(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.mp3'):
            convertirMp3AAvi(self.archivoEntrada)

    def convertir_a_mkv(self):
        if self.archivoEntrada.endswith('.mp4'):
            convertir_mp4_a_mkv(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.avi'):
            convertirAviAMkv(self.archivoEntrada)
        elif self.archivoEntrada.endswith('.mp3'):
            convertirMp3AMkv(self.archivoEntrada)


if __name__ == "__main__":
    raiz = TkinterDnD.Tk()
    app = aplicacionConvertidorVideo(raiz)
    raiz.mainloop()
