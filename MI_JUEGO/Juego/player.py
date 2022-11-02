import pygame
from constantes import *

def getSurfaceFromSpriteSheet(path, columnas, filas, flip = False):
    lista = []
    surface_imagen = pygame.image.load(path)

    fotograma_ancho = int(surface_imagen.get_width() / columnas)
    fotograma_alto = int(surface_imagen.get_height() / filas)

    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            #print(x, y, fotograma_ancho, fotograma_alto)
            surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            if flip:
                surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)   # True es el x, False el y
            lista.append(surface_fotograma)
    return lista


class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity) -> None:
        self.walk_r = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\walk.png", 15, 1)[:12]
        self.walk_l = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\walk.png", 15, 1, True)[:12]
        self.stay_r = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\idle.png", 16, 1)
        self.stay_l = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\idle.png", 16, 1, True)
        self.jump = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\jump.png", 33, 1)
        self.climb = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\climb.png", 19, 1)
        self.happy = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\happy.png", 21, 1)
        self.sleep = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\sleep.png", 22, 1) # tiene dos filas de 22 NOSE
        self.surprise = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\surprise.png", 21, 1)
        self.angry = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\angry.png", 20, 1)
        
        self.frame = 0                          # que fotograma de todos muestro
        self.lives = 5
        self.score = 0
        self.mover_x = x
        self.mover_y = y
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.animation = self.angry
        self.image = self.animation[self.frame] # agarro esa imagen en particular y despues pido el rectangulo
        self.rect = self.image.get_rect()


    def walking(self):
        pass
    def staying(self):
        pass
    def jumping(self):
        pass
    def climbing(self):
        pass

    def control(self, action):

        if(action == "WALK_R"):
            self.mover_x = self.speed_walk
            self.animation = self.walk_r
            self.frame = 0
        elif(action == "WALK_L"):
            self.mover_x = -self.speed_walk
            self.animation = self.walk_l
            self.frame = 0
        elif(action == "STAY_R"):
            self.mover_x = 0
            self.mover_y = 0
            self.animation = self.stay_r
            self.frame = 0
        elif(action == "STAY_L"):
            self.mover_x = 0
            self.mover_y = 0
            self.animation = self.stay_l
            self.frame = 0
        elif(action == "JUMP"):
            self.animation = self.jump
            self.frame = 0
        elif(action == "CLIMB"):
            self.animation = self.climb
            self.frame = 0
        elif(action == "HAPPY"):
            self.animation = self.happy
            self.frame = 0
        elif(action == "SLEEP"):
            self.animation = self.sleep
            self.frame = 0
        elif(action == "SURPRISE"):
            self.animation = self.surprise
            self.frame = 0
        elif(action == "ANGRY"):
            self.animation = self.angry
            self.frame = 0

    def update(self):
        if(self.frame < len(self.animation ) -1):
            self.frame += 1
        else:
            self.frame = 0

        self.rect.x += self.mover_x
        self.rect.y += self.mover_y

        if(self.rect.y < 500):
            self.rect.y += self.gravity

    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)              #que quiero fundir, donde la quiero fundir

