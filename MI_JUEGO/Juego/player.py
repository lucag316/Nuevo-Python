import pygame
from constantes import *
from auxiliar import *

class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump, frame_rate_ms, move_rate_ms, height_jump, interval_time_jump = 100) -> None: # p_scale podria agregar, no se bien que es
        # self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12] del profe
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\walk.png", 15, 1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\walk.png", 15, 1, True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\idle.png", 16, 1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\idle.png", 16, 1, True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\jump.png", 33, 1, False, 2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\jump.png", 33, 1, True, 2)
        self.climb = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\climb.png", 19, 1)
        self.happy = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\happy.png", 21, 1)
        self.sleep = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\sleep.png", 22, 1) # tiene dos filas de 22 NOSE
        self.surprise = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\surprise.png", 21, 1)
        self.angry = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\green_hat\angry.png", 20, 1)
        
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
        self.start_jump_y = 0
        self.height_jump = height_jump

        self.animation = self.stay_r
        self.image = self.animation[self.frame] # agarro esa imagen en particular y despues pido el rectangulo
        self.rect = self.image.get_rect(x = x, y = y)
        # self.rect.x = x   # donde empieza el personaje
        # self.rect.y = y   # donde empieza el personaje

        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 4, GROUND_RECT_H)
        self.rect_cuerpo = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y, self.rect.w / 3.5, self.rect.h)

        self.is_jump = False
        self.is_fall = False
        # self.is_shoot = False
        # self.is_knife = False

        self.tiempo_transcurrido_animacion = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump


    def walking(self, direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                
            if(direction == DIRECTION_RIGHT):
                self.mover_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.mover_x = -self.speed_walk
                self.animation = self.walk_l

    # def shoot(self,on_off = True):
    #     self.is_shoot = on_off
    #     if(on_off == True and self.is_jump == False and self.is_fall == False):
    #         if(self.animation != self.shoot_r and self.animation != self.shoot_l):
    #             self.frame = 0
    #             self.is_shoot = True
    #             if(self.direction == DIRECTION_R):
    #                 self.animation = self.shoot_r
    #             else:
    #                 self.animation = self.shoot_l       

    # def knife(self,on_off = True):
    #     self.is_knife = on_off
    #     if(on_off == True and self.is_jump == False and self.is_fall == False):
    #         if(self.animation != self.knife_r and self.animation != self.knife_l):
    #             self.frame = 0
    #             if(self.direction == DIRECTION_R):
    #                 self.animation = self.knife_r
    #             else:
    #                 self.animation = self.knife_l  


    def jumping(self, on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False): # and self.is_fall == False
            self.start_jump_y = self.rect.y
            if(self.direction == DIRECTION_RIGHT):
                self.mover_x = int(self.mover_x / 2) #self.speed_walk     # int(self.move_x / 2)
                self.mover_y = -self.jump
                self.animation = self.jump_r
            else:
                self.mover_x = int(self.mover_x / 2) #-self.speed_walk # int(self.move_x / 2)
                self.mover_y = -self.jump
                self.animation = self.jump_l

            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.staying()

    def staying(self):
        # if(self.is_knife or self.is_shoot):
        #     return
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_RIGHT):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.mover_x = 0
            self.mover_y = 0
            self.frame = 0
            
    def add_x(self, delta_x): # para mover los rectangulos #CHANGE X (BUEN NOMBRE PARA EL METODO)
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_cuerpo.x += delta_x

    def add_y(self, delta_y):  # para mover los rectangulos
        self.rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_cuerpo.y += delta_y

    def do_movement(self, delta_ms, lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.start_jump_y) - abs(self.rect.y) > self.height_jump and self.is_jump):
                self.mover_y = 0

            self.tiempo_transcurrido_move = 0 # CREO QUE NO VA
            self.add_x(self.mover_x)
            self.add_y(self.mover_y)

            if(not self.is_on_platform(lista_plataformas)):
                if(self.mover_y == 0):
                    self.is_fall = True
                    self.add_y(self.gravity) # esto iria adentro del if de arriba
            else:
                if (self.is_jump): 
                    self.jumping(False)
                self.is_fall = False

    def is_on_platform(self, lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if self.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                    retorno = True
                    break

        return retorno

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if(self.tiempo_transcurrido_animacion >= self.frame_rate_ms): # cada cuantos  milisegundos se actualiza el frame(fotograma) (frame_rate_ms)
            self.tiempo_transcurrido_animacion = 0

            if(self.frame < len(self.animation) -1):
                self.frame += 1
            else:
                self.frame = 0

    def update(self, delta_ms, lista_plataformas):
        self.do_movement(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)
        #podriamos separar la  gravedad tambien
    
    def draw(self, screen):
        if(DEBUG):
        #    pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, BLUE, self.rect_cuerpo)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)              #que quiero fundir, donde la quiero fundir
        
    def events_keys(self, keys, delta_ms): # si fuera ej el enemigo le puedo poner tiempo ( 2 seg para la derecha, 2 seg para laizquierda)
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walking(DIRECTION_LEFT)

        if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.walking(DIRECTION_RIGHT)

        if(not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]):
            self.staying()

        if(keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_UP]):
            self.staying()

        if(keys[pygame.K_UP]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jumping(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

    #         if(not keys[pygame.K_a]):
    #             self.shoot(False)  

    #         if(not keys[pygame.K_a]):
    #             self.knife(False)  

    #         if(keys[pygame.K_s] and not keys[pygame.K_a]):
    #             self.shoot()   
            
    #         if(keys[pygame.K_a] and not keys[pygame.K_s]):
    #             self.knife()   




















    # def climbing(self):
    #     pass

    # def control(self, action):

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
        