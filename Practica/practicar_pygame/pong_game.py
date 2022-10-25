import pygame, sys, random

pygame.init()

#definir  colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NARANJA = (255, 102, 0)
MARRON = (133, 59, 9)
ROSA = (255, 0, 157)

screen_size = (800, 600) # tamaño de la ventana
screen = pygame.display.set_mode(screen_size) # creo la ventana
clock = pygame.time.Clock()

player_width = 15    # ancho del jugador
player_height = 90       #alto del jugador



# coordenadas y velocidad del JUGADOR UNO
player_one_coordenada_x = 50
player_one_coordenada_y = 300 - (player_height / 2) # 300 - 45
player_one_speed_y = 0

# coordenadas y velocidad del JUGADOR DOS
player_two_coordenada_x = 750 - player_width
player_two_coordenada_y = 300 - (player_height / 2)
player_two_speed_y = 0

# coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3                 #le asigno directo el valor porque no depende de que presione algo para que se mueva
pelota_speed_y = 3                 #lo mismo
game_over = False

while not game_over:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_over = True
        if(event.type == pygame.KEYDOWN):
            # jugador 1
            if(event.key == pygame.K_w):
                player_one_speed_y = -3
            if(event.key == pygame.K_s):
                player_one_speed_y = 3
            # jugador 2
            if(event.key == pygame.K_UP):
                player_two_speed_y = -3
            if(event.key == pygame.K_DOWN):
                player_two_speed_y = 3
        
        if(event.type == pygame.KEYUP):
            # jugador 1
            if(event.key == pygame.K_w):
                player_one_speed_y = 0
            if(event.key == pygame.K_s):
                player_one_speed_y = 0
            # jugador 2
            if(event.key == pygame.K_UP):
                player_two_speed_y = 0
            if(event.key == pygame.K_DOWN):
                player_two_speed_y = 0


    if(pelota_y > 590 or pelota_y < 10):
        pelota_speed_y *= -1

    # revisa si la pelota sale de los lados
    if(pelota_x < 0 or pelota_x > 800):
        pelota_x = 400
        pelota_y = 300
        # si sale de la pantalla, invierte la direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1


            

    # Modifica las coordenadas para dar movimiento a los jugadores y a la pelota
    player_one_coordenada_y += player_one_speed_y
    player_two_coordenada_y += player_two_speed_y

    # Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y


    screen.fill(WHITE) # pinta el fondo 

    #---------ZONA DE DIBUJO
    jugador_uno = pygame.draw.rect(screen, NARANJA, (player_one_coordenada_x, player_one_coordenada_y, player_width, player_height))
    jugador_dos = pygame.draw.rect(screen, NARANJA, (player_two_coordenada_x, player_two_coordenada_y, player_width, player_height))
    pelota = pygame.draw.circle(screen, MARRON, (pelota_x, pelota_y), 10)
    #---------ZONA DE DIBUJO


    # COLICIONES
    if(pelota.colliderect(jugador_uno) or pelota.colliderect(jugador_dos)):
        pelota_speed_x *= -1


    pygame.display.flip() # actualiza la  ventana
    clock.tick(60)
    
pygame.quit()
