# Desafío #00:

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

from data_stark import lista_personajes

# def mostrar(lista:list):
#     '''
#     Muestra mas prolijo a los personajes de la lista que recibe

#     Recibe una lista
#     '''
#     for elemento in lista:
#         print("Nombre: {0} \nIdentidad: {1} \nEmpresa: {2} \nAltura: {3} \nGenero: {4} \nColor de ojos: {5} \nColor de pelo: {6} \nFuerza: {7}\nInteligencia: {8}".format(elemento["nombre"], elemento["identidad"], elemento["empresa"], elemento["altura"], elemento["genero"], elemento["color_ojos"], elemento["color_pelo"], elemento["fuerza"], elemento["inteligencia"]))


def analizar_set_datos(lista_personajes:list):
    '''
    Recorre toda la lista de personajes e imprime cada diccionario

    Recibe una lista
    '''
    for personaje in lista_personajes:
        print(personaje)

#-------------------------------------------PUNTO A-----------------------------------------------------------------------
#analizar_set_datos(lista_personajes)

def imprimir_nombres(lista_personajes:list):
    '''
    Imprime por consola el nombre de cada personaje
    
    Recibe la lista de personajes
    '''
    for personaje in lista_personajes:
        print("Nombre: {0}".format(personaje["nombre"]))

#-------------------------------------------PUNTO B-----------------------------------------------------------------------
#imprimir_nombres(lista_personajes)

def  imprimir_nombres_alturas(lista_personajes:list):
    '''
    Imprime por consola el nombre de cada personaje junto su altura

    Recibe la lista de personajes
    '''
    for personaje in lista_personajes:
        print("Nombre: {0}    -     Altura: {1}".format(personaje["nombre"], personaje["altura"]))

#-------------------------------------------PUNTO C-----------------------------------------------------------------------
#imprimir_nombres_alturas(lista_personajes)


def buscar_personaje_mas_alto(lista_personajes:list):
    '''
    Busca en la lista de personajes al mas alto

    Recibe la listade personajes

    Retorna al personaje mas alto
    '''
    personaje_mas_alto = lista_personajes[0]

    for personaje in lista_personajes:

        if(type(personaje["altura"]) != type(float())):
            personaje["altura"] = float(personaje["altura"])

        if(type(personaje["peso"]) != type(float())):
            personaje["peso"] = float(personaje["peso"])

        if(type(personaje["fuerza"]) != type(int())):
            personaje["fuerza"] = int(personaje["fuerza"])


        if(personaje["altura"] > personaje_mas_alto["altura"]):
            personaje_mas_alto = personaje

    return personaje_mas_alto
#-------------------------------------------PUNTO D-----------------------------------------------------------------------
#print(buscar_personaje_mas_alto(lista_personajes))


def buscar_personaje_mas_bajo(lista_personajes:list):
    '''
    Busca en la lista de personajes al mas bajo

    Recibe la listade personajes

    Retorna al personaje mas bajo
    '''
    personaje_mas_bajo = lista_personajes[0]

    for personaje in lista_personajes:

        if(type(personaje["altura"]) != type(float())):
            personaje["altura"] = float(personaje["altura"])

        if(type(personaje["peso"]) != type(float())):
            personaje["peso"] = float(personaje["peso"])

        if(type(personaje["fuerza"]) != type(int())):
            personaje["fuerza"] = int(personaje["fuerza"])


        if(personaje["altura"] < personaje_mas_bajo["altura"]):
            personaje_mas_bajo = personaje

    return personaje_mas_bajo
#-------------------------------------------PUNTO E-----------------------------------------------------------------------
#print(buscar_personaje_mas_bajo(lista_personajes))

def buscar_altura_promedio(lista_personajes:list):
    '''
    Busca en la lista de personajes la altura promedio

    Recibe la lista

    Retorna la altura promedio
    '''

    acumulador_alturas = 0
    cantidad_personajes = 0

    for personaje in lista_personajes:

        if(type(personaje["altura"]) != type(float())):
            personaje["altura"] = float(personaje["altura"])

        acumulador_alturas  += personaje["altura"]
        cantidad_personajes += 1

    promedio_altura = acumulador_alturas / cantidad_personajes

    return promedio_altura
#-------------------------------------------PUNTO F----------------------------------------------------------------------
#print(buscar_altura_promedio(lista_personajes))

def informar_nombres_asociados_puntos_anteriores(lista_personajes:list):
    '''
    informa el nombre de cada uno de los personajes asociados a los puntos anteriores

    Recibe la lista

    Devuelve el nombre de los personajes de los anteriores puntos
    '''
    personaje_mas_alto = buscar_personaje_mas_alto(lista_personajes)
    personaje_mas_bajo = buscar_personaje_mas_bajo(lista_personajes)

    mensaje = "El nombre del personaje mas alto es: {0} \nEl nombre del personaje mas bajo es: {1}".format(personaje_mas_alto["nombre"], personaje_mas_bajo["nombre"])

    return mensaje
#-------------------------------------------PUNTO G-----------------------------------------------------------------------
#print(informar_nombres_asociados_puntos_anteriores(lista_personajes))


def calcular_personaje_mas_y_menos_pesado(lista_personajes:list):
    '''
    Busca en la lista al personaje mas y menos pesado

    Recibe la lista de personajes

    Retorna a los dos personajes
    '''

    for personaje in lista_personajes:
        pass
#-------------------------------------------PUNTO H-----------------------------------------------------------------------

# H- Calcular e informar cual es el superhéroe más y menos pesado.
# I- Ordenar el código implementando una función para cada uno de los valores informados.
# J- Construir un menú que permita elegir qué dato obtener

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

#FALTA TEMINAR