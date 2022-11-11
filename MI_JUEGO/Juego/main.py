import pygame, sys
from constantes import *
from player import Player
from enemigo import *
from plataforma import Platform
# from pygame.locals import *    no se que es

DEBUG = True

pygame.init()

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) # screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\mountain\all.png") # .convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

#player_one = Player(0, 0, 4, 8, 15) forma mas fea
player_one = Player(x = 0, y = 300, speed_walk = 4, speed_run = 8, gravity = 10, jump = 20, frame_rate_ms = 20, move_rate_ms = 10, height_jump = 150) #frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)

# enemy_one = Jabba(400, 450, 200, 500, 15)
#enemy_two = Gelatina(200,450, 20)
# enemy_three = Piedra(600, 525)
# enemy_four = Hongo(330, 330)
#enemy_four = Rude(700, 450)

orco = OrkAxe(400, 75, 3, 150, 950)
orco_martillo = OrkHammer(1050, 225, 0)
orco_espada = OrkSword(450, 355, 5, 425, 900)
coco = Coconut()

plataforma_x = 400
plataforma_y = 505
plataforma_w = 50
plataforma_h = 50

lista_plataformas = []
# plataform_list.append(Plataform(x=650,y=430,width=50,height=50,type=14)) ejemplo
while plataforma_x < 1000:
    lista_plataformas.append(Platform(plataforma_x, plataforma_y, plataforma_w, plataforma_h, 4)) # el ultimo es el tipo(el cuadradode tierra)
    plataforma_x += 50

plataforma_x_2 = 1000
while plataforma_x_2 < 1150:
    lista_plataformas.append(Platform(plataforma_x_2, 375, 50, 50, 4))
    plataforma_x_2 += 50

plataforma_x_3 = 50
while plataforma_x_3 < 1000:
    lista_plataformas.append(Platform(plataforma_x_3, 225, 50, 50, 4))
    plataforma_x_3 += 50

# lista_plataformas.append(Platform(480,500,50,50,1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        '''
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     player_one.walking(DIRECTION_RIGHT)
            # if event.key == pygame.K_LEFT:
            #     player_one.walking(DIRECTION_LEFT)

            if event.key == pygame.K_UP:
                player_one.jumping(True)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_one.jumping(False)
          
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player_one.control("WALK_R")
        #     if event.key == pygame.K_LEFT:
        #         player_one.control("WALK_L")

        #     if event.key == pygame.K_UP:
        #         player_one.control("JUMP_R")

        # if event.type == pygame.KEYUP:    
        #     if event.key == pygame.K_RIGHT:
        #         player_one.control("STAY_R")
        #     if event.key == pygame.K_LEFT:
        #         player_one.control("STAY_L")

        #     if event.key == pygame.K_UP:
        #         player_one.control("STAY_R")
        '''

    keys = pygame.key.get_pressed()
    
    delta_ms = clock.tick(FPS) 
    screen.blit(imagen_fondo, imagen_fondo.get_rect())


    # DIBUJO LAS PLATAFORMAS
    for plataforma in lista_plataformas:
        plataforma.draw(screen)

    # ---------PLAYER UPDATE------------- verifica como el player intercatua con todo el nivel
    player_one.events_keys(keys, delta_ms)
    player_one.update(delta_ms, lista_plataformas)
    player_one.draw(screen)
    # ---------PLAYER UPDATE-------------


    #----------ENEMIGOS UPDATE-----------
    orco.controlar_ruta()
    orco.update()
    orco.mover()
    orco.draw(screen)
    orco.colicion(player_one.rect_cuerpo)
    
    orco_martillo.update()
    orco_martillo.draw(screen)
    orco_martillo.colicion(player_one.rect_cuerpo)
    
    orco_espada.controlar_ruta()
    orco_espada.update()
    orco_espada.mover()
    orco_espada.draw(screen)
    orco_espada.colicion(player_one.rect_cuerpo)


    coco.update()
    coco.draw(screen)
    coco.colicion(player_one.rect_cuerpo)

    # enemy_one.controlar_ruta()
    # enemy_one.update()
    # enemy_one.draw(screen)
    # enemy_one.mover()
    # enemy_one.colicion(player_one.rect)


    # enemy_two.update()
    # enemy_two.draw(screen)
    # enemy_two.mover()
    # enemy_two.colicion(player_one.rect)

    # enemy_three.update()
    # enemy_three.draw(screen)
    # enemy_three.colicion(player_one.rect)

    # enemy_four.update()
    # enemy_four.draw(screen)
    # enemy_four.colicion(player_one.rect)

    #----------ENEMIGOS UPDATE-----------


    #----------DIBUJAR PLAYER------------
    #----------DIBUJAR PLAYER------------

    #----------DIBUJAR TODOO EL NIVEL---------------
    #----------DIBUJAR TODOO EL NIVEL---------------


    #print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()

    #print(delta_ms)