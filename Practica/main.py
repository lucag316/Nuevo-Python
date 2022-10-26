import pygame
import colores

pygame.init()

ANCHO_VENTANA = 1200
ALTO_VENTANA = 700

screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
pygame.display.set_caption("Luca Game")

running = True

posicion_circulo = [200, 600]


# TIMER
timer_segundo = pygame.USEREVENT
pygame.time.set_timer(timer_segundo, 10)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos) # marca la posicion en donde haces click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #posicion_circulo = list(event.pos) # donde hago click pone el centro del circulo
            print(event.pos)
        if event.type == pygame.USEREVENT:
            if event.type == timer_segundo:
                print("ya paso un segundo")
                # if posicion_circulo[0] > 400:
                #     posicion_circulo[0] *= -1
                #     if posicion_circulo[0] < 200:
                #         posicion_circulo[0] *= 1
                if(posicion_circulo[0] < ANCHO_VENTANA + 10):
                    posicion_circulo[0] = posicion_circulo[0] + 1 # corre el circulo (al tiempo que le ponga en [pygame.time.set_timer(timer_segundo, 10)])

                else:
                    posicion_circulo[0] = -10
                    # ESTE IF ELSE LO PUEDO  USAR POR EJEMPLO SI QUIERO QUE EL FONDO SE VEA MOVIENDOSE, EJEMPLO UN AUTO EN LA RUTA AVANZANDO
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                pass
            if event.type == pygame.K_RIGHT:
                pass
            if event.type == pygame.K_UP:
                pass
            if event.type == pygame.K_DOWN:
                pass
            








    screen.fill(colores.WHITE)

    #---------------ZONA DE DIBUJO------------------
    pygame.draw.rect(screen, colores.ORANGE, (0, 600, 1200, 700)) # donde empieza x, y, donde terminan x, y
    pygame.draw.circle(screen, colores.BROWN, posicion_circulo, 10)
    pygame.draw. rect(screen, colores.BLACK, (20, 550, 50, 50))

    #---------------ZONA DE DIBUJO------------------      
      

    pygame.display.flip()
pygame.quit()

