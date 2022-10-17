# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# C- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
# D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
# G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
# H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
# I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# J- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# M- Listar todos los superhéroes agrupados por color de ojos.
# N- Listar todos los superhéroes agrupados por color de pelo.
# O- Listar todos los superhéroes agrupados por tipo de inteligencia
from ast import Return
from data_stark import lista_personajes

'''
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''
#########################################################################################################################
def normalizar_datos(lista_personajes:list):

    for personaje in lista_personajes:

        personaje["altura"] = float(personaje["altura"])
        personaje["peso"] = float(personaje["peso"])
        personaje["fuerza"] = int(personaje["fuerza"])

normalizar_datos(lista_personajes)

def buscar_primer_femenino(lista_personajes:list)->dict:
    '''
    Busca el primer femenino

    Recibe una lista

    Retorna un diccionario
    '''
    for personaje in lista_personajes:

        if(personaje["genero"] == "F"):

            return personaje

def buscar_primer_masculino(lista_personajes:list)->dict:
    '''
    Busca el primer masculino

    Recibe una lista

    Retorna un diccionario
    '''
    for personaje in lista_personajes:

        if(personaje["genero"] == "M"):

            return personaje

def crear_lista_femeninos(lista_personajes:list)->list:

    lista_femeninos = []

    for personaje in lista_personajes:

        if(personaje["genero"] == "F"):
            lista_femeninos.append(personaje)

    return lista_femeninos

def crear_lista_masculinos(lista_personajes:list)->list:

    lista_masculinos = []

    for personaje in lista_personajes:

        if(personaje["genero"] == "M"):
            lista_masculinos.append(personaje)

    return lista_masculinos

lista_femeninos = crear_lista_femeninos(lista_personajes)

lista_masculinos = crear_lista_masculinos(lista_personajes)

def buscar_max_min_indice(lista_personajes:list, clave:str, tipo:str)->int:
    '''
    Busca el maximo o minimo, segun el usuario quiera

    Recibe la lista, una clave, y el tipo (maximo o minimo)

    Retorna un entero
    '''
    max_min = 0

    for indice in range(len(lista_personajes)):
        
        if(tipo == "maximo" and lista_personajes[indice][clave] > lista_personajes[max_min][clave]):
            max_min = indice

        elif(tipo == "minimo" and lista_personajes[indice][clave] < lista_personajes[max_min][clave]):
                max_min = indice

    return max_min

def buscar_max_min(lista_personajes:list, clave:str, tipo:str):

    for personaje in p


##########################################################################################################################
def imprimir_nombres_masculinos(lista_personajes:list):
    '''
    Imprime todos los nombres de los personajes masculinos

    Recibe una lista
    '''
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):
            print(personaje["nombre"])
#-----------------------------------------PUNTO A-------------------------------------------------------------------------
def imprimir_nombre_femeninos(lista_personajes:list):
    '''
    Imprime todos los nombres de los personajes femeninos

    Recibe una lista
    '''
    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):
            print(personaje["nombre"])
#-----------------------------------------PUNTO B-------------------------------------------------------------------------

def buscar_masculino_mas_alto(lista_personajes:list):
    '''
    Busca al personaje masculino mas alto y lo retorna
    '''
    personaje_mas_alto = lista_personajes[0]

    for personaje in lista_personajes:

        if(personaje["genero"] == "M"):

            if(personaje["altura"] > personaje_mas_alto["altura"]):
                personaje_mas_alto = personaje

        #personaje_mas_alto = "Nombre: {0} \nIdentidad: {1} \nEmpresa: {2} \nAltura: {3} \nGenero: {4} \nColor de ojos: {5} \nColor de pelo: {6} \nFuerza: {7}\nInteligencia: {8}".format(personaje_mas_alto["nombre"], personaje_mas_alto["identidad"], personaje_mas_alto["empresa"], personaje_mas_alto["altura"], personaje_mas_alto["genero"], personaje_mas_alto["color_ojos"], personaje_mas_alto["color_pelo"], personaje_mas_alto["fuerza"], personaje_mas_alto["inteligencia"])

    return personaje_mas_alto
#-----------------------------------------PUNTO C-------------------------------------------------------------------------

def buscar_femenino_mas_alto(lista_personajes:list):
    '''
    Busca al personaje femenino mas alto y lo retorna
    '''
    femenino_mas_alto = buscar_max_min(lista_personajes, "altura", "maximo")

    return femenino_mas_alto

#-----------------------------------------PUNTO D-------------------------------------------------------------------------
print(buscar_femenino_mas_alto(lista_femeninos))

# D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
# G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
# H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
# I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# J- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# M- Listar todos los superhéroes agrupados por color de ojos.
# N- Listar todos los superhéroes agrupados por color de pelo.
# O- Listar todos los superhéroes agrupados por tipo de inteligencia