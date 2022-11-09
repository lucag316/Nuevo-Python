import pygame
from constantes import *
from auxiliar import Auxiliar

# aca podria haber un metodo o un json para hacer lista de plataformas

class Platform:
    def __init__(self, x, y, w, h, type = 0) -> None:
        self.image = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\luca_\Desktop\Nuevo python\Nuevo-Python\MI_JUEGO\Recursos\sheet1.png", 8, 8)[type]
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

    def draw(self, screen):
        if(DEBUG):
            pygame.draw.rect(screen, RED, self.rect)
        screen.blit(self.image, self.rect)

        if(DEBUG):
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)






# class Plataform:
#     def __init__(self, x, y,width, height,  type=1):

#         self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",18,flip=False,w=width,h=height)
        
#         self.image = self.image_list[type]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.collition_rect = pygame.Rect(self.rect)
#         self.ground_collition_rect = pygame.Rect(self.rect)
#         self.ground_collition_rect.height = GROUND_COLLIDE_H

#     def draw(self,screen):
#         screen.blit(self.image,self.rect)
#         if(DEBUG):
#             pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
#             pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        