import pygame

class Personaje:
    '''
    Se puede documentar la clase
    '''
    def __init__(self, nombre:str,  edad:int, vida:int, genero:str, password:str) -> None:
        # ES MEJOR PONER LOS ATRIBUTOS SOLO EN EL __INIT__  para no confundir
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.genero = genero
        self.__password = password



    # def mostrar(self):
    #     print(self.nombre)
    #     print(self.edad)
    #     print(self.vida)
    #     print(self.genero)


    # def get_nombre(self):
    #     return self.nombre

    # def set_nombre(self, nombre):
    #     self.nombre = nombre
    @property                                   # GET   getters
    def nombre(self):
        return self.nombre

    @nombre.setter                              # SET   setters
    def nombre(self, nombre):
        self.nombre = nombre

    def comer(self):
        pass
    def dormir(self):
        pass
    def atacar(self):
        pass
    def defender(self):
        pass



aux_personaje = Personaje("Luca", 19, 100, "Masculino", "contraseña")
print(aux_personaje.nombre)