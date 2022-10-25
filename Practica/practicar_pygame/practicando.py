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
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

lista_coordenadas = []

for i  in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    lista_coordenadas.append([x, y])

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()

    screen.fill(WHITE)

    # for coordenada in lista_coordenadas:
    #     x = coordenada[0]
    #     y = coordenada[1]
    #     pygame.draw.circle(screen, NARANJA, (x, y), 5)
    #ES LO MISMO
    for coordenada in lista_coordenadas:

        pygame.draw.circle(screen, NARANJA, coordenada, 5)

        coordenada[1] += 1 #van cayendo los que son y
        if(coordenada[1] > 500):
            coordenada[1] = 0 #para que cuando lleguen al final, vuelvan a caer

    pygame.display.flip()
    clock.tick(60)



