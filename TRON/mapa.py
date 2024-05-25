# Github: https://github.com/Lucased12

import pygame

blanco = (255, 255, 255)
ancho, alto = 800, 600

def dibujarCuadricula(pantalla):
    tamanio_celda = 20  #Tamanio de cada celda en la cuadrícula
    for x in range(0, ancho, tamanio_celda):
        pygame.draw.line(pantalla, blanco, (x, 0), (x, alto))
    for y in range(0, alto, tamanio_celda):
        pygame.draw.line(pantalla, blanco, (0, y), (ancho, y))

def dibujarBorde(pantalla):
    grosorBorde = 10  #grosor del borde
    pygame.draw.rect(pantalla, blanco, (0, 0, ancho, grosorBorde))  #borde arriba
    pygame.draw.rect(pantalla, blanco, (0, 0, grosorBorde, alto))  #izquierda
    pygame.draw.rect(pantalla, blanco, (0, alto - grosorBorde, ancho, grosorBorde))  #abajo
    pygame.draw.rect(pantalla, blanco, (ancho - grosorBorde, 0, grosorBorde, alto))  #derecha
