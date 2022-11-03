import pygame

class Auxiliar:

    @staticmethod
    def getSurfaceFromSpriteSheet(path,  columnas, filas, flip = False, step = 1) -> None:

        lista = []

        surface = pygame.image.load(path)

        fotograma_ancho = surface.get_width() // columnas 
        fotograma_alto = surface.get_height() // filas

        for fila in range(filas):
            for columna in range(0, columnas, step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto

                surface_fotograma = surface.subsurface(x, y, fotograma_ancho, fotograma_alto)
                if flip:
                    surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)

                lista.append(surface_fotograma)
        return lista
