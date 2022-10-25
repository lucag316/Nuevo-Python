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

#crear ventana
screen = pygame.display.set_mode(size)

#controlar los FPS 
clock = pygame.time.Clock()


#cordenadas
cordenada_x = 100
cordenada_y = 100

#velocidad a  la que  se movera 
speed_x = 3
speed_y = 3
 
while True:

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
    
    if(cordenada_x > 700 or cordenada_x < 0):
        speed_x *= -1
    if(cordenada_y > 400 or cordenada_y < 0):
        speed_y *= -1

    cordenada_x += speed_x
    cordenada_y += speed_y

    #----------ZONA DE LOGICA


    #----------ZONA DE LOGICA


    #color de fondo                                          con la escala rgb se ponen los colores
    screen.fill(WHITE) #pinta la pantalla de blanco, color de fondo


    ###-------ZONA DE DIBUJO                                     tiene que estar despues de pintar el fondo

    pygame.draw.line(screen, RED, [400, 200], [400, 300], 100) #[donde empieza X, Y], [donde termina X, Y], grosor
    pygame.draw.line(screen, BLACK, [400, 100], [400, 200], 100)
    pygame.draw.circle(screen, BLUE, (100, 100), 50)
    pygame.draw.rect(screen, GREEN, (cordenada_x, cordenada_y, 80, 80))
    #pygame.draw.circle(surface, color, center, radius)
    #pygame.draw.rect(surface, color, rect)
    for x in range(50, 350, 50): # (donde queremos inciar, donde queremos finalizar, el salto entre cada uno)
        pygame.draw.line(screen, NARANJA, (x, 0), (x, 150), 10)
    
    for y in range(50,350, 50):
        pygame.draw.line(screen, ROSA, (0, y), (300, y), 10)

    cordenada_x += speed_x
    cordenada_y += speed_y
    

    ###-------ZONA DE DIBUJO


    #actualizar pantalla
    pygame.display.flip() #actualiza la pantalla 
    clock.tick(60)