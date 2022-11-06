import pygame
from constantes import *

def getSurfaceFromSpriteSheet(path, columnas, filas, flip = False, step = 1):
    lista = []
    surface_imagen = pygame.image.load(path)

    fotograma_ancho = int(surface_imagen.get_width() / columnas)
    fotograma_alto = int(surface_imagen.get_height() / filas)
    x = 0

    for fila in range(filas):
        for columna in range(0, columnas, step):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            #print(x, y, fotograma_ancho, fotograma_alto)
            surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            if flip:
                surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)   # True es el x, False el y
            lista.append(surface_fotograma)
    return lista

class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump, frame_rate_ms, move_rate_ms) -> None:
        self.walk_r = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\walk.png", 15, 1)[:12]
        self.walk_l = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\walk.png", 15, 1, True)[:12]
        self.stay_r = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\idle.png", 16, 1)
        self.stay_l = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\idle.png", 16, 1, True)
        self.jump_r = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\jump.png", 33, 1, False, 2)
        self.jump_l = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\jump.png", 33, 1, True, 2)
        self.climb = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\climb.png", 19, 1)
        self.happy = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\happy.png", 21, 1)
        self.sleep = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\sleep.png", 22, 1) # tiene dos filas de 22 NOSE
        self.surprise = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\surprise.png", 21, 1)
        self.angry = getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\angry.png", 20, 1)
        
        self.frame = 0                          # que fotograma de todos muestro
        self.lives = 5
        self.score = 0
        self.mover_x = 0
        self.mover_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.direction = DIRECTION_RIGHT

        self.jump = jump
        self.is_jump = False

        self.animation = self.angry
        self.image = self.animation[self.frame] # agarro esa imagen en particular y despues pido el rectangulo
        self.rect = self.image.get_rect()

        self.rect.x = x   # donde empieza el personaje
        self.rect.y = y   # donde empieza el personaje

        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animacion = 0
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms


    def walking(self, direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.direction = direction
            self.frame = 0

        if(direction == DIRECTION_RIGHT):
            self.mover_x = self.speed_walk
            self.animation = self.walk_r
        else:
            self.mover_x = -self.speed_walk
            self.animation = self.walk_l


    def staying(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_RIGHT):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l

            self.mover_x = 0
            self.mover_y = 0
            self.frame = 0
            

    def jumping(self, on_off = True):
        if(on_off and self.is_jump == False):
            if(self.direction == DIRECTION_RIGHT):
                self.mover_x = self.speed_walk
                self.mover_y = -self.jump
                self.animation = self.jump_r
            else:
                self.mover_x = -self.speed_walk
                self.mover_y = -self.jump
                self.animation = self.jump_l

            self.frame = 0
            self.is_jump = True
        else:
            self.is_jump = False
            self.staying()


    def climbing(self):
        pass

    def control(self, action):

    #     if(action == "WALK_R"):
    #         self.mover_x = self.speed_walk
    #         self.animation = self.walk_r
    #         self.frame = 0
    #     elif(action == "WALK_L"):
    #         self.mover_x = -self.speed_walk
    #         self.animation = self.walk_l
    #         self.frame = 0

    #     if(action == "STAY_R"):
    #         self.mover_x = 0
    #         self.mover_y = 0
    #         self.animation = self.stay_r
    #         self.frame = 0
    #         self.is_jump = False
    #     elif(action == "STAY_L"):
    #         self.mover_x = 0
    #         self.mover_y = 0
    #         self.animation = self.stay_l
    #         self.frame = 0
    #         self.is_jump = False

    #     elif(action == "JUMP_R"):
    #         self.mover_y = -self.jump
    #         self.mover_x = self.speed_walk
    #         self.animation = self.jump_r
    #         self.frame = 0
    #         self.is_jump = True
    #     elif(action == "JUMP_L"):
    #         self.animation = -self.jump
    #         self.animation = self.jump_l
    #         self.frame = 0
    #         self.is_jump = True

    #     elif(action == "CLIMB"):
    #         self.animation = self.climb
    #         self.frame = 0
    #     elif(action == "HAPPY"):
    #         self.animation = self.happy
    #         self.frame = 0
    #     elif(action == "SLEEP"):
    #         self.animation = self.sleep
    #         self.frame = 0
    #     elif(action == "SURPRISE"):
    #         self.animation = self.surprise
    #         self.frame = 0
    #     elif(action == "ANGRY"):
    #         self.animation = self.angry
    #         self.frame = 0
        pass


    def do_movement(self, delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.rect.x += self.mover_x
            self.rect.y += self.mover_y

            if(self.rect.y < 500):
                self.rect.y += self.gravity

    def do_animation(self, delta_ms):

        self.tiempo_transcurrido_animacion += delta_ms
        if(self.tiempo_transcurrido_animacion >= self.frame_rate_ms): # cada cuantos  milisegundos se actualiza el frame(fotograma) (frame_rate_ms)
            self.tiempo_transcurrido_animacion = 0

            if(self.frame < len(self.animation) -1):
                self.frame += 1
            else:
                self.frame = 0



    def update(self, delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        #podriamos separar la  gravedad tambien
    
    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)              #que quiero fundir, donde la quiero fundir

