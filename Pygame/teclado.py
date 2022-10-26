import pygame, sys, random
pygame.init()

#definir  colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NARANJA = (237, 118, 14)
ROSA = (255, 0, 157)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


#Coordenadas del cuadrado
coordenada_x = 10
coordenada_y = 10

#velocidad de coordenadas
speed_x = 0
speed_y = 0

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()

        #EVENTOS TECLADO
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                speed_x = -3
            if(event.key == pygame.K_RIGHT):
                speed_x = 3

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT):
                speed_x = 0
            if(event.key == pygame.K_RIGHT):
                speed_x = 0

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_UP):
                speed_y = -3
            if(event.key == pygame.K_DOWN):
                speed_y = 3

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_UP):
                speed_y = 0
            if(event.key == pygame.K_DOWN):
                speed_y = 0

    screen.fill(WHITE)

    coordenada_x += speed_x
    coordenada_y += speed_y

    pygame.draw.rect(screen, RED, (coordenada_x, coordenada_y, 100, 100))

    pygame.display.flip()
    clock.tick(60)