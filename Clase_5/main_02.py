from data_stark import lista_personajes
import re
from Desafio_02 import *


def stark_marvel_app(lista_personajes:list):
    '''
    '''
    while True:

        respuesta = stark_menu_principal()

        if(respuesta == 1):
            stark_imprimir_nombres_heroes(lista_personajes)
        elif(respuesta == 2):
            stark_imprimir_nombres_alturas(lista_personajes)
        elif(respuesta == 3):

            key = input("Ingrese la clave que desea calcular (altura, peso,  fuerza):  ")
            while(key  != "altura" and key != "peso" and key != "fuerza"):
                key = input("ERROR, reingrese la clave que desea calcular (altura, peso,  fuerza):  ")

            tipo = input("Ingrese el tipo de calculo(maximo o minimo):  ")
            while(tipo != "maximo" and  tipo != "minimo"):
                tipo = input("ERROR, reingrese el tipo de calculo(maximo o minimo):  ")

            stark_calcular_imprimir_heroe(lista_personajes, key, tipo)
        elif(respuesta == 4):

            key = input("Ingrese la clave que desea calcular (altura, peso,  fuerza):  ")
            while(key  != "altura" and key != "peso" and key != "fuerza"):
                key = input("ERROR, reingrese la clave que desea calcular (altura, peso,  fuerza):  ")

            variable = calcular_promedio(lista_personajes, key)
            variable = round(variable, 2) #solo dosnumeros despues de la coma
            print(variable)
        elif(respuesta == 5):
            stark_calcular_imprimir_promedio_altura(lista_personajes)
        elif(respuesta == 6):
            break
        
#----------------------------------------------7----------------------------------------------------------------------
stark_marvel_app(lista_personajes)


