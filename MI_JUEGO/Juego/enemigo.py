import pygame
from auxiliar import *

# class EnemigoBase:
#     def __init__(self, x, y) -> None:
        
#         self.vida = 1
#         self.frame = 0

#         self.animation = self.walk
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.move_x = 0
#         self.move_y = 0

        # def update(self):
                
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

class Jabba:
    def __init__(self, x, y) -> None:
        self.vida = 1
        self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_talk_end_png_1354831104.png", 2, 7)
        self.walk = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_walk_png_1354831096.png", 2, 7)
        self.frame = 0

        self.animation = self.walk
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0

    def mover(self):
        self.move_x = +1
        self.rect.x += self.move_x
        self.animation = self.walk

        
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


class Gelatina:
    def __init__(self, x, y) -> None:
        self.vida = 1
        self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_jabba1\npc_jabba1__x1_talk_end_png_1354831104.png", 2, 7)
        self.walk = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_juju_yellow\npc_juju_yellow__x1_move_left_end_png_1354831777.png", 8, 2)
        self.frame = 0

        self.animation = self.walk
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        

    def mover(self):
        self.move_x = -1
        self.rect.x += self.move_x
        self.animation = self.walk


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













# class Piedra:

#     def __init__(self, x, y) -> None:
#         self.vida = 1
#         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_fox_ranger\npc_fox_ranger__x1_idle2_png_1354839637.png", 15, 6)
#         self.frame = 0

#         self.animation = self.stay
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.move_x = 0
#         self.move_y = 0

    
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












# class Hongo:

#     def __init__(self, x, y) -> None:
#         self.vida = 1
#         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\street_spirit_zutto\street_spirit_zutto_cap_capAqua_x1_lower_png_1354833718.png", 6, 5)
#         self.frame = 0

#         self.animation = self.stay
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.move_x = 0
#         self.move_y = 0

    
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











# class Rude:

#     def __init__(self, x, y) -> None:
#         self.vida = 1
#         self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\npc_rube\npc_rube__x1_spawn_in_png_1354831067.png", 9, 22)
#         self.frame = 0

#         self.animation = self.stay
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.move_x = 0
#         self.move_y = 0

    
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