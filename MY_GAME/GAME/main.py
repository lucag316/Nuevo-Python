import pygame, sys
from constantes import *

pygame.init()

screen = pygame.display.set_mode(ANCHO_VENTANA, ALTO_VENTANA)
clock = pygame.time.Clock()
imagen_fondo = pygame.image.load("").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    
    delta_ms = clock.tick(FPS) 
    screen.blit(imagen_fondo, imagen_fondo.get_rect())
    
    pygame.display.flip()