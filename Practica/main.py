import pygame
import colores

pygame.init()

ANCHO_VENTANA = 1200
ALTO_VENTANA = 700

screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
pygame.display.set_caption("Luca Game")

running = True
flag_mostrar_texto_segundos = False


posicion_circulo = [200, 600]
posicion_circulo_2 = [100, 600]

coordenada_x = 20
coordenada_y = 550

speed_x = 0
speed_y = 0

# TIMER
timer = pygame.USEREVENT
pygame.time.set_timer(timer, 10)
timer_5_seg = pygame.USEREVENT
pygame.time.set_timer(timer_5_seg, 5000)


# LEER UNA IMAGEN
imagen_dona = pygame.image.load(r"Nuevo-Python\Practica\Recursos\00.png")
imagen_dona = pygame.transform.scale(imagen_dona,(50, 50))

background = pygame.image.load(r"Nuevo-Python\Practica\Recursos\background.png")
background = pygame.transform.scale(background, (1200, 700))


# CREAR UN TEXTO
fuente = pygame.font.SysFont("Arial", 30) # el numero es la altura
texto = fuente.render("Bienvenido a Luca Game", True, colores.BROWN) # lo transforma en una imagen(al texto), tipo superficie

texto_segundos = pygame.font.SysFont("Arial", 30)
texto_segundos = texto_segundos.render("Ya pasaron 5 segundos", True, colores.RED)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos) # marca la posicion en donde haces click
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_circulo_2 = list(event.pos) # donde hago click pone el centro del circulo
            #print(event.pos)
        if event.type == pygame.USEREVENT:
            if event.type == timer_5_seg:
                flag_mostrar_texto_segundos = True

            if event.type == timer:
                #print("ya paso un x segundo")
                # if posicion_circulo[0] > 400:
                #     posicion_circulo[0] *= -1
                #     if posicion_circulo[0] < 200:
                #         posicion_circulo[0] *= 1
                if(posicion_circulo[0] < ANCHO_VENTANA + 10):
                    posicion_circulo[0] = posicion_circulo[0] + 1 # corre el circulo (al tiempo que le ponga en [pygame.time.set_timer(timer_segundo, 10)])

                else:
                    posicion_circulo[0] = -10
                    # ESTE IF ELSE LO PUEDO  USAR POR EJEMPLO SI QUIERO QUE EL FONDO SE VEA MOVIENDOSE, EJEMPLO UN AUTO EN LA RUTA AVANZANDO


        # EVENTOS TECLADO
        if(event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_LEFT):
                speed_x = -1
            if(event.key == pygame.K_RIGHT):
                speed_x = 1
            if(event.key == pygame.K_UP):
                speed_y = -1
            if(event.key == pygame.K_DOWN):
                speed_y = 1
            
            if(event.key == pygame.K_a):                    # CON ESTA FORMA NO SE PUEDE MANTENER
                posicion_circulo_2[0] = posicion_circulo_2[0] - 10
            if(event.key == pygame.K_d):
                posicion_circulo_2[0] = posicion_circulo_2[0] + 10
            if(event.key == pygame.K_w):
                posicion_circulo_2[1] = posicion_circulo_2[1] - 10
            if(event.key == pygame.K_s):
                posicion_circulo_2[1] = posicion_circulo_2[1] + 10
            
            
        if(event.type == pygame.KEYUP):

            if(event.key == pygame.K_LEFT):
                speed_x = 0
            if(event.key == pygame.K_RIGHT):
                speed_x = 0
            if(event.key == pygame.K_UP):
                speed_y = 0
            if(event.key == pygame.K_DOWN):
                speed_y = 0

            if(event.key == pygame.K_a):                    # CON ESTA FORMA NO SE PUEDE MANTENER
                posicion_circulo_2[0]
            if(event.key == pygame.K_d):
                posicion_circulo_2[0]
            if(event.key == pygame.K_w):
                posicion_circulo_2[1]
            if(event.key == pygame.K_s):
                posicion_circulo_2[1]
            

    # lista_teclas = pygame.key.get_pressed()  #        FORMA DEL PROFE PARA QUE SI SE PUEDA MANTENER
    # if  lista_teclas[pygame.K_a]:                      # en cada vuelta del while lo lee, no es por eventos esta forma
    #     posicion_circulo_2[0] = posicion_circulo_2[0] - 0.1

    screen.fill(colores.WHITE)

    coordenada_x += speed_x
    coordenada_y += speed_y

    #---------------ZONA DE DIBUJO----------------------------------------
    screen.blit(background, (0, 0))
    #pygame.draw.rect(screen, colores.ORANGE, (0, 600, 1200, 700)) # donde empieza x, y, donde terminan x, y
    pygame.draw.circle(screen, colores.BROWN, posicion_circulo, 10)
    pygame.draw.circle(screen, colores.PINK, posicion_circulo_2, 30)
    pygame.draw.rect(screen, colores.BLACK, [coordenada_x, coordenada_y, 50, 50])

    screen.blit(imagen_dona, (150, 150)) # posicion
    screen.blit(texto, (450, 50))
    if flag_mostrar_texto_segundos: # si esta flag esta en true ...
        screen.blit(texto_segundos, (10, 20))
    #---------------ZONA DE DIBUJO----------------------------------------      

    pygame.display.flip()
pygame.quit()

