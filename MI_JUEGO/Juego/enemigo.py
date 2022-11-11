import pygame
from auxiliar import *
from constantes import *

class EnemigoBase:
    def __init__(self, cordenada_x, cordenada_y, speed_walk, animacion) -> None:
        
        self.vida = 1
        self.frame = 0

        self.animation = animacion # que reciba como parametro
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(x = cordenada_x, y = cordenada_y)

        self.move_x = 0
        self.move_y = 0

        self.speed_walk = speed_walk
        self.direction = DIRECTION_RIGHT

    def update(self):
            if(self.frame < len(self.animation) -1):
                self.frame += 1
            else:
                self.frame = 0

    def draw(self, screen):
        if self.vida == 1:

            self.image = self.animation[self.frame]
            screen.blit(self.image, self.rect)

    def colicion(self, pos_xy):
        if(self.rect.colliderect(pos_xy)):
            self.vida = 0



class Coconut(EnemigoBase):
    def __init__(self, cordenada_x, cordenada_y, speed_walk, animacion) -> None:
        # self.stay = "C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\street_spirit_groddle\street_spirit_groddle_base_base_L1wood_bottom_bottom_L1woodRoots_eyes_eyes_L1eyes1_skull_skull_L1wood_top_top_L1woodLeafHat_x1_idle_hold_png_1354835649.png")
        # "C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\street_spirit_groddle\street_spirit_groddle_base_base_L1wood_bottom_bottom_L1woodRoots_eyes_eyes_L1eyes2_skull_skull_L1wood_top_top_L1woodLeafHat_x1_idle_move_png_1354835704.png")

        self.atack = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\street_spirit_groddle\street_spirit_groddle_base_base_L1wood_bottom_bottom_L1woodRoots_eyes_eyes_L1eyes3_skull_skull_L1wood_top_top_L1woodLeafHat_x1_open_png_1354835735.png", )
        
        super().__init__(cordenada_x, cordenada_y, speed_walk, animacion)




class OrkAxe(EnemigoBase):
    def __init__(self, x, y, speed_walk, minimo_x, maximo_x) -> None:
        #self.stay = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\ork_hammer\IDLE\idle_00{0}.png", 6, False, 1, 1, 120, 150, 7)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\ork_axe\WALK\walk_00{0}.png", 6, False, 1, 1, 120, 150, 7)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\ork_axe\WALK\walk_00{0}.png", 6, True, 1, 1, 120, 150, 7)
        
        super().__init__(x, y, speed_walk, self.walk_r)

        self.minimo_x = minimo_x
        self.maximo_x = maximo_x
        self.retrocediendo = False

    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.x > self.minimo_x:
                self.animation = self.walk_l
                self.move_x = -self.speed_walk
            else:
                self.retrocediendo = False
        else:
            if self.rect.x < self.maximo_x:
                self.animation = self.walk_r
                self.move_x = self.speed_walk
            else:
                self.retrocediendo = True
    
    def mover(self):
        self.rect.x += self.move_x

class OrkHammer(EnemigoBase):
    def __init__(self, x, y, speed_walk) -> None:
        self.stay = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\ork_hammer\IDLE\idle_00{0}.png", 6, True, 1, 1, 120, 150, 7)
        super().__init__(x, y, speed_walk, self.stay)
        

class OrkSword(EnemigoBase):
    def __init__(self, x, y, speed_walk, minimo_x, maximo_x) -> None:
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\ork_sword\RUN\run_00{0}.png", 6, False, 1, 1, 120, 150, 7)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\ork_sword\RUN\run_00{0}.png", 6, True, 1, 1, 120, 150, 7)
        super().__init__(x, y, speed_walk, self.run_r)
        
        self.minimo_x = minimo_x
        self.maximo_x = maximo_x
        self.retrocediendo = False


    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.x > self.minimo_x:
                self.animation = self.run_l
                self.move_x = -self.speed_walk
            else:
                self.retrocediendo = False
        else:
            if self.rect.x < self.maximo_x:
                self.animation = self.run_r
                self.move_x = self.speed_walk
            else:
                self.retrocediendo = True
    
    def mover(self):
        self.rect.x += self.move_x


class Gelatina:
    def __init__(self, x, y, speed_walk) -> None:
        self.vida = 1
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_talk_end_png_1354831104.png", 2, 7)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_talk_end_png_1354831104.png", 2, 7, True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_move_left_end_png_1354831777.png", 8, 2)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_move_left_end_png_1354831777.png", 8, 2, True)
        self.morir_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_shrink_png_1354831791.png", 8, 6)
        self.morir_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_shrink_png_1354831791.png", 8, 6, True)
        self.aparecer_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_spawn_png_1354831774.png", 8, 8)
        self.aparecer_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_spawn_png_1354831774.png", 8, 8, True)
        self.frame = 0

        self.speed_walk = speed_walk
        self.animation = self.stay_l
        self.image = self.animation[self.frame]
        #self.rect_pos = pygame.Rect(x+55,y+110,80,80) 
        #self.rect = pygame.Rect(x,y,50,50)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.move = 0
        

    def mover(self):
        self.move_x = -1
        self.rect.x += self.move_x
        self.animation = self.walk


    def update(self):
        if(self.frame < len(self.animation) -1):
            self.frame += 1
        else:
            self.frame = 0

        # if(self.move <= 400):
        #         self.move_x = -self.speed_walk
        #         self.animation = self.walk_l
        #         self.move += 1
        # elif(self.move <= 800):
        #     self.move_x = self.speed_walk
        #     self.animation = self.walk_r
        #     self.move += 1
        # else:
        #     self.move = 0

    def draw(self, screen):
        if self.vida == 1:

            self.image = self.animation[self.frame]
            screen.blit(self.image, self.rect)

    
    def colicion(self, pos_xy):
        if(self.rect.colliderect(pos_xy)):
            self.vida = 0



# class Jabba:
#     def __init__(self, x, y, minimo_x, maximo_x, velocidad) -> None:
#         self.vida = 1
#         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_talk_end_png_1354831104.png", 2, 7)
#         self.walk = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_walk_png_1354831096.png", 2, 7)
#         self.frame = 0

#         self.animation = self.walk
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.move_x = 0
#         self.move_y = 0
#         self.retrocediendo = False
#         self.minimo_x = minimo_x
#         self.maximo_x = maximo_x
#         self.velocidad = velocidad

#     def mover(self):
#         self.rect.x += self.move_x
#         self.animation = self.walk

#     def controlar_ruta(self):
#         if self.retrocediendo:
#             if self.rect.x > self.minimo_x:
#                 self.move_x = -self.velocidad
#             else:
#                 self.retrocediendo = False
#         else:
#             if self.rect.x < self.maximo_x:
#                 self.move_x = self.velocidad
#             else:
#                 self.retrocediendo = True

#     def update(self):
        
#         if(self.frame < len(self.animation) -1):
#             self.frame += 1
#         else:
#             self.frame = 0

#     def draw(self, screen):

#         if self.vida == 1:

#             self.image = self.animation[self.frame]
#             screen.blit(self.image, self.rect)

    
#     def colicion(self, pos_xy):
#         if(self.rect.colliderect(pos_xy)):
#             self.vida = 0


# class Gelatina:
#     def __init__(self, x, y) -> None:
#         self.vida = 1
#         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_talk_end_png_1354831104.png", 2, 7)
#         self.walk = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_move_left_end_png_1354831777.png", 8, 2)
#         self.frame = 0

#         self.animation = self.walk
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.move_x = 0
#         self.move_y = 0
        

#     def mover(self):
#         self.move_x = -1
#         self.rect.x += self.move_x
#         self.animation = self.walk


#     def update(self):
#         if(self.frame < len(self.animation) -1):
#             self.frame += 1
#         else:
#             self.frame = 0

#     def draw(self, screen):
#         if self.vida == 1:

#             self.image = self.animation[self.frame]
#             screen.blit(self.image, self.rect)

    
#     def colicion(self, pos_xy):
#         if(self.rect.colliderect(pos_xy)):
#             self.vida = 0












# # class Piedra:

# #     def __init__(self, x, y) -> None:
# #         self.vida = 1
# #         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_fox_ranger\npc_fox_ranger__x1_idle2_png_1354839637.png", 15, 6)
# #         self.frame = 0

# #         self.animation = self.stay
# #         self.image = self.animation[self.frame]
# #         self.rect = self.image.get_rect()
# #         self.rect.x = x
# #         self.rect.y = y
# #         self.move_x = 0
# #         self.move_y = 0

    
# #     def update(self):
# #         if(self.frame < len(self.animation) -1):
# #             self.frame += 1
# #         else:
# #             self.frame = 0

# #     def draw(self, screen):
# #         if self.vida == 1:

# #             self.image = self.animation[self.frame]
# #             screen.blit(self.image, self.rect)

    
# #     def colicion(self, pos_xy):
# #         if(self.rect.colliderect(pos_xy)):
# #             self.vida = 0












# # class Hongo:

# #     def __init__(self, x, y) -> None:
# #         self.vida = 1
# #         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\street_spirit_zutto\street_spirit_zutto_cap_capAqua_x1_lower_png_1354833718.png", 6, 5)
# #         self.frame = 0

# #         self.animation = self.stay
# #         self.image = self.animation[self.frame]
# #         self.rect = self.image.get_rect()
# #         self.rect.x = x
# #         self.rect.y = y
# #         self.move_x = 0
# #         self.move_y = 0

    
# #     def update(self):
# #         if(self.frame < len(self.animation) -1):
# #             self.frame += 1
# #         else:
# #             self.frame = 0

# #     def draw(self, screen):
# #         if self.vida == 1:

# #             self.image = self.animation[self.frame]
# #             screen.blit(self.image, self.rect)

    
# #     def colicion(self, pos_xy):
# #         if(self.rect.colliderect(pos_xy)):
# #             self.vida = 0











# # class Rude:

# #     def __init__(self, x, y) -> None:
# #         self.vida = 1
# #         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_rube\npc_rube__x1_spawn_in_png_1354831067.png", 9, 22)
# #         self.frame = 0

# #         self.animation = self.stay
# #         self.image = self.animation[self.frame]
# #         self.rect = self.image.get_rect()
# #         self.rect.x = x
# #         self.rect.y = y
# #         self.move_x = 0
# #         self.move_y = 0

    
# #     def update(self):
# #         if(self.frame < len(self.animation) -1):
# #             self.frame += 1
# #         else:
# #             self.frame = 0

# #     def draw(self, screen):
# #         if self.vida == 1:

# #             self.image = self.animation[self.frame]
# #             screen.blit(self.image, self.rect)

    
# #     def colicion(self, pos_xy):
# #         if(self.rect.colliderect(pos_xy)):
# #             self.vida = 0