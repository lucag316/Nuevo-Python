import pygame

screen = pygame.display.set_mode([1200, 600])

timer = pygame.time.Clock()

#definir  colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NARANJA = (237, 118, 14)
ROSA = (255, 0, 157)



running = True


background = pygame.image.load("\Nuevo python\Nuevo-Python\Pygame\Recursos\background.png").convert()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, [0, 0])

    pygame.display.flip()

    timer.tick(60)

pygame.quit()