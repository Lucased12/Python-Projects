# Github: https://github.com/Lucased12

import pygame
import sys
from player import Jugador
import mapa  

pygame.init()

ancho, alto = 800, 600
negro = (0, 0, 0)

def verificarChoque(jugador, oponente):
    x, y = jugador.posiciones[-1]
    if x < 0 or x >= ancho or y < 0 or y >= alto:
        return True  
    
    if jugador.posiciones[-1] in jugador.estela[:-1] or jugador.posiciones[-1] in oponente.estela:
        return True  
    return False

def principal():
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Tron")
    
    icono = pygame.image.load("icon.ico")
    pygame.display.set_icon(icono)

    jugador1 = Jugador((0, 0, 255), (0, 255, 255), (100, alto // 2), [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
    jugador2 = Jugador((255, 165, 0), (255, 255, 0), (ancho - 100, alto // 2), [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    reloj = pygame.time.Clock()  #crea un clock para controlar la velocidad de actualización de la pantalla
    paused = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            jugador1.mover()
            jugador2.mover()

            if verificarChoque(jugador1, jugador2):
                print("Juego terminado! Jugador 2 es el ganador!")
                pygame.quit()
                sys.exit()
            elif verificarChoque(jugador2, jugador1):
                print("Juego terminado! Jugador 1 es el ganador!")
                pygame.quit()
                sys.exit()

        pantalla.fill(negro)
        mapa.dibujarCuadricula(pantalla)  
        mapa.dibujarBorde(pantalla)  
        jugador1.dibujar(pantalla)
        jugador2.dibujar(pantalla)
        pygame.display.flip()

        reloj.tick(10)  #pone al juego a 10 fps

if __name__ == "__main__":
    principal()
