import pygame, sys
from constantes import *
from player import Player
from enemigo import *

pygame.init()

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\mountain\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

#player_one = Player(0, 0, 4, 8, 15) forma mas fea
player_one = Player(x = 0, y = 0, speed_walk = 4, speed_run = 8, gravity = 15, jump = 20) #podria agregarle el jump por ejemplo

enemy_one = Jabba(500, 450)
enemy_two = Gelatina(200,450)
enemy_three = Piedra(600, 525)
#enemy_four = Rude(700, 450)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_one.control("WALK_R")
            if event.key == pygame.K_LEFT:
                player_one.control("WALK_L")

            if event.key == pygame.K_UP:
                player_one.control("JUMP_R")

        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_RIGHT:
                player_one.control("STAY_R")
            if event.key == pygame.K_LEFT:
                player_one.control("STAY_L")

            if event.key == pygame.K_UP:
                player_one.control("STAY_R")

    screen.blit(imagen_fondo, imagen_fondo.get_rect())
    # ---------PLAYER UPDATE------------- verifica como el player intercatua con todo el nivel
    player_one.update()
    player_one.draw(screen)
    # ---------PLAYER UPDATE-------------


    #----------ENEMIGOS UPDATE-----------
    enemy_one.update()
    enemy_one.draw(screen)
    enemy_one.mover()
    enemy_one.colicion(player_one.rect)


    enemy_two.update()
    enemy_two.draw(screen)
    enemy_two.mover()
    enemy_two.colicion(player_one.rect)

    enemy_three.update()
    enemy_three.draw(screen)
    enemy_three.colicion(player_one.rect)

    # enemy_four.update()
    # enemy_four.draw(screen)
    # enemy_four.colicion(player_one.rect)

    #----------ENEMIGOS UPDATE-----------


    #----------DIBUJAR PLAYER------------
    #----------DIBUJAR PLAYER------------

    #----------DIBUJAR TODOO EL NIVEL---------------
    #----------DIBUJAR TODOO EL NIVEL---------------

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)
