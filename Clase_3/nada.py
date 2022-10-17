# A- Analizar detenidamente el set de datos
# B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C- Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# D- Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E- Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F- Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# G- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# H- Calcular e informar cual es el superhéroe más y menos pesado.
# I- Ordenar el código implementando una función para cada uno de los valores informados.
# J- Construir un menú que permita elegir qué dato obtener
from __future__ import print_function
from data_stark import lista_personajes

def imprimir_nombres_heroes():
    for heroe in lista_personajes:
       print("Nombre: {0} ".format(heroe["nombre"]))
def imprimir_nombres_y_alturas():
    for personaje in lista_personajes:
        nombre_personaje = personaje["nombre"]
        altura_personaje = float(personaje["altura"])
        print("Nombre: {0} \nAltura: {1}".format(nombre_personaje, altura_personaje))
def calcular_nombre_mas_alto():
    personaje_altura_mayor = lista_personajes[0]

    for personaje in lista_personajes:
        if(float(personaje["altura"]) > float(personaje_altura_mayor["altura"])):
            personaje_altura_mayor = personaje

    print("El nombre del personaje mas alto es: {0} con una altura de: {1}".format(personaje_altura_mayor["nombre"], personaje_altura_mayor["altura"]))
def calcular_mas_del_bajo():
    personaje_altura_menor = lista_personajes[0]

    for personaje in lista_personajes:
        if(float(personaje["altura"]) < float(personaje_altura_menor["altura"])):
            personaje_altura_menor = personaje

    print("El nomnbre del personaje mas bajo es: {0} con una altura de: {1}".format(personaje_altura_menor["nombre"], personaje_altura_menor["altura"]))
def altura_promedio_heroes():
    acumulador_alturas = 0
    contador = 0
    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        acumulador_alturas += altura
        contador += 1

    promedio = acumulador_alturas / contador
    print("el promedio de altura es: {0}".format(promedio))
def calcular_nombre_asociados():
    personaje_mayor = lista_personajes[0]
    personaje_menor = lista_personajes[0]
    for personaje in lista_personajes:
        if(float(personaje["altura"]) > float(personaje_mayor["altura"])):
            personaje_mayor = personaje

        if(float(personaje["altura"]) < float(personaje_menor["altura"])):
            personaje_menor = personaje


    print("El personaje mas alto es: {0}".format(personaje_mayor["nombre"]))
    print("El personaje mas bajo es: {0}".format(personaje_menor["nombre"]))
def gordo_flaco():
    mas_gordo = lista_personajes[0]
    mas_flaco = lista_personajes[0]
    for personaje in lista_personajes:
        if(float(personaje["peso"]) > float(mas_gordo["peso"])):
            mas_gordo = personaje
        if(float(personaje["peso"]) < float(mas_flaco["peso"])):
            mas_flaco = personaje

    print("mas pesado: {0} menos pesado: {1}".format(mas_gordo["nombre"], mas_flaco["nombre"]))


# I- Ordenar el código implementando una función para cada uno de los valores informados.
# J- Construir un menú que permita elegir qué dato obtener


while True:
    respuesta = input("1- imprimir_nombres_heroes \n2- imprimir_nombres_y_alturas \n3- calcular_nombre_mas_alto \n4- calcular_mas_del_bajo \n5- altura_promedio_heroes \n6- calcular_nombre_asociados \n7- gordo_flaco \n8- Para salir \nQue desea saber?: ")

    if(respuesta == "1"):
        imprimir_nombres_heroes()
    elif(respuesta == "2"):
        imprimir_nombres_y_alturas()
    elif(respuesta == "3"):
        calcular_nombre_mas_alto()
    elif(respuesta == "4"):
        calcular_mas_del_bajo()
    elif(respuesta == "5"):
        altura_promedio_heroes()
    elif(respuesta == "6"):
        calcular_nombre_asociados()
    elif(respuesta == "7"):
        gordo_flaco()
    elif(respuesta == "8"):
        break
