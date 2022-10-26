
class Persona:
    def __init__(self,id) -> None:
        self.id = id
    def mostrar(self):
        print(self.id)
    def get_id(self):
        return self.id

class Personaje(Persona):
    def __init__(self,nombre="") -> None:
        super().__init__(88)
        self.__nombre = nombre
        self.apellido = ""
        self.lista = ["HOLA","PEPE"]
    
    def get_id(self):
        return float(super().get_id())

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    def __str__(self):
        return self.__nombre + "HOLA "
    def __len__(self):
        return 8
    def __getitem__(self,index):
        if(index == "nombre"):
            return self.__nombre
        else:
            return ""
    def __setitem__(self,index,valor):
        if(index == "nombre"):
            self.__nombre = valor

    def __iter__(self):
        for i in self.lista:
            yield i

    


aux = Personaje("Vero")
aux["nombre"] = "JUAN"
'''
print(aux["nombre"])
print(aux.nombre)

contador = 0
for elemento in aux:
    contador+=1
    print(elemento)
print(contador)
'''

print(aux.get_id())
