# Github: https://github.com/Lucased12

import pygame

class Jugador:
    def __init__(self, color, colorEstela, posInicial, teclas, longitudEstela=25):
        self.color = color
        self.colorEstela = colorEstela
        self.direccion = "arriba"
        self.teclas = teclas
        self.posiciones = [posInicial]
        self.estela = []
        self.longitudEstela = longitudEstela
    
    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[self.teclas[0]] and self.direccion != "abajo":
            self.direccion = "arriba"
        elif teclas[self.teclas[1]] and self.direccion != "arriba":
            self.direccion = "abajo"
        elif teclas[self.teclas[2]] and self.direccion != "derecha":
            self.direccion = "izquierda"
        elif teclas[self.teclas[3]] and self.direccion != "izquierda":
            self.direccion = "derecha"
            #ve que tecla se esta moviendo y lo mueve y tambien ve para que no vuelva en
            #la misma direccion

        x, y = self.posiciones[-1]
        if self.direccion == "arriba":
            y -= 10
        elif self.direccion == "abajo":
            y += 10
        elif self.direccion == "izquierda":
            x -= 10
        elif self.direccion == "derecha":
            x += 10
        
        self.posiciones.append((x, y))
        self.estela.append((x, y))  

        if len(self.estela) > self.longitudEstela:
            del self.estela[0]

    def dibujar(self, pantalla):
        for i in range(1, len(self.estela)):
            pygame.draw.line(pantalla, self.colorEstela, self.estela[i-1], self.estela[i], 10)
        x, y = self.posiciones[-1]
        pygame.draw.rect(pantalla, self.color, (x - 5, y - 5, 10, 10))
