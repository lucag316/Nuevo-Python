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

def normalizar_datos(lista_personajes:list):

    for personaje in lista_personajes:

        personaje["altura"] = float(personaje["altura"])
        personaje["peso"] = float(personaje["peso"])
        personaje["fuerza"] = int(personaje["fuerza"])
normalizar_datos(lista_personajes)
# def mostrar(personaje:dict):

#     print("Nombre: {0} \nIdentidad: {1} \nEmpresa: {2} \nAltura: {3} \nGenero: {4} \nColor de ojos: {5} \nColor de pelo: {6} \nFuerza: {7}\nInteligencia: {8}".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))

def analizar_set_datos(lista_personajes:list):
    '''
    Recorre toda la lista de personajes e imprime cada diccionario

    Recibe una lista
    '''
    for personaje in lista_personajes:
        print(personaje)
#-------------------------------------------PUNTO A-----------------------------------------------------------------------

def imprimir_nombres(lista_personajes:list):
    '''
    Imprime por consola el nombre de cada personaje
    
    Recibe la lista de personajes
    '''
    for personaje in lista_personajes:
        print("Nombre: {0}".format(personaje["nombre"]))
#-------------------------------------------PUNTO B-----------------------------------------------------------------------

def  imprimir_nombres_alturas(lista_personajes:list):
    '''
    Imprime por consola el nombre de cada personaje junto su altura

    Recibe la lista de personajes
    '''
    for personaje in lista_personajes:
        print("Nombre: {0}    -     Altura: {1}".format(personaje["nombre"], personaje["altura"]))
#-------------------------------------------PUNTO C-----------------------------------------------------------------------

def calcular_personaje_mas_alto(lista_personajes:list):
    '''
    Busca en la lista de personajes al mas alto

    Recibe la listade personajes

    Retorna al personaje mas alto
    '''
    personaje_mas_alto = lista_personajes[0]

    for personaje in lista_personajes:

        if(personaje["altura"] > personaje_mas_alto["altura"]):
            personaje_mas_alto = personaje

    return personaje_mas_alto
#-------------------------------------------PUNTO D-----------------------------------------------------------------------

def calcular_personaje_mas_bajo(lista_personajes:list):
    '''
    Busca en la lista de personajes al mas bajo

    Recibe la listade personajes

    Retorna al personaje mas bajo
    '''
    personaje_mas_bajo = lista_personajes[0]

    for personaje in lista_personajes:

        if(personaje["altura"] < personaje_mas_bajo["altura"]):
            personaje_mas_bajo = personaje

    return personaje_mas_bajo
#-------------------------------------------PUNTO E-----------------------------------------------------------------------

def calcular_altura_promedio(lista_personajes:list):
    '''
    Busca en la lista de personajes la altura promedio

    Recibe la lista

    Retorna la altura promedio
    '''

    acumulador_alturas = 0
    cantidad_personajes = 0

    for personaje in lista_personajes:

        acumulador_alturas  += personaje["altura"]
        cantidad_personajes += 1

    promedio_altura = acumulador_alturas / cantidad_personajes

    return promedio_altura
#-------------------------------------------PUNTO F----------------------------------------------------------------------

def informar_nombres_asociados_puntos_anteriores(lista_personajes:list):
    '''
    informa el nombre de cada uno de los personajes asociados a los puntos anteriores

    Recibe la lista

    Devuelve el nombre de los personajes de los anteriores puntos
    '''
    personaje_mas_alto = calcular_personaje_mas_alto(lista_personajes)
    personaje_mas_bajo = calcular_personaje_mas_bajo(lista_personajes)

    mensaje = "El nombre del personaje mas alto es: {0} \nEl nombre del personaje mas bajo es: {1}".format(personaje_mas_alto["nombre"], personaje_mas_bajo["nombre"])

    return mensaje
#-------------------------------------------PUNTO G-----------------------------------------------------------------------

def calcular_personaje_mas_y_menos_pesado(lista_personajes:list):
    '''
    Busca en la lista al personaje mas y menos pesado

    Recibe la lista de personajes

    Retorna a los dos personajes
    '''
    personaje_mas_pesado = lista_personajes[0]
    personaje_menos_pesado = lista_personajes[0]

    for personaje in lista_personajes:

        if(personaje["peso"] > personaje_mas_pesado["peso"]):
            personaje_mas_pesado = personaje
        
        elif(personaje["peso"] < personaje_menos_pesado["peso"]):
            personaje_menos_pesado = personaje

    mensaje = "El personaje mas pesado es: {0} \nEl personaje menos pesado es: {1}".format(personaje_mas_pesado, personaje_menos_pesado)

    return mensaje
#-------------------------------------------PUNTO H-----------------------------------------------------------------------

def menu():
    while True:
        print("1- Analizar set de datos \n2- Nombrar a todos los personajes \n3- Nombre y altura de los personajes \n4- Personaje mas alto \n5- Personaje mas bajo \n6- Promedio de altura \n7- Nombre del personaje mas alto y mas bajo \n8- Personaje mas y menos pesado \n9- Salir")

        respuesta = input()

        if(respuesta == "1"):
            analizar_set_datos(lista_personajes)
        elif(respuesta == "2"):
            imprimir_nombres(lista_personajes)
        elif(respuesta == "3"):
            imprimir_nombres_alturas(lista_personajes)
        elif(respuesta == "4"):
            print(calcular_personaje_mas_alto(lista_personajes))
        elif(respuesta == "5"):
            print(calcular_personaje_mas_bajo(lista_personajes))
        elif(respuesta == "6"):
            print(calcular_altura_promedio(lista_personajes))
        elif(respuesta == "7"):
            print(informar_nombres_asociados_puntos_anteriores(lista_personajes))
        elif(respuesta == "8"):
            print(calcular_personaje_mas_y_menos_pesado(lista_personajes))
        elif(respuesta == "9"):
            break
menu()