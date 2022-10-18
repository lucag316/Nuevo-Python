from data_stark import lista_personajes
import re
'''
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
'''
def extraer_iniciales(nombre_heroe:str) -> str :
    '''
    La funcion toma el nombre del personaje y agarra las inciales, si el string esta vacion devuelve N/A, sino las inciales

    Recibe por paramertro el nombre del personaje

    Devuelve un nuevo string con las inciales del personaje
    '''
    retorno = "N/A"
    iniciales = ""

    if(type(nombre_heroe) == type(str()) and len(nombre_heroe) > 0):
        nombre_heroe = nombre_heroe.upper()
        nombre_heroe = nombre_heroe.replace("THE ", "")
        if(nombre_heroe.count("-") > 0):
            nombre_heroe = nombre_heroe.replace("-", " ")
        
        nombre_heroe = nombre_heroe.split(" ")
        partes_nombre = nombre_heroe

        for parte in partes_nombre:
            iniciales += parte[0] + "."

        retorno = iniciales
    
    return retorno
#------------------------------------------------1.1------------------------------------------------------------------
#print(extraer_iniciales(lista_personajes[0]["nombre"]))


def definir_iniciales_nombre(heroe:dict):
    '''
    Agrega una  clave (iniciales) al  diccionario recibido y su valor es el de la funcion ‘extraer_iniciales’

    Recibe por parametro al diccionario del personaje
    '''
    retorno = False
    if(type(heroe) == type(dict())):
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        retorno = True

    return retorno
#------------------------------------------------1.2------------------------------------------------------------------
print(definir_iniciales_nombre(lista_personajes[0]))

#FALTA VALIDAR QUE EL DICCIONARIO CONTENGA  LA  CLAVE NOMBRE












def agregar_iniciales_nombre():
    '''
    '''
#------------------------------------------------1.3------------------------------------------------------------------
# 1.3- Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como parámetro:
# lista_heroes: lista de personajes
# 	Se deberá validar:
# Que lista_heroes sea del tipo lista
# Que la lista contenga al menos un elemento
# La función deberá iterar la lista_heroes pasándole cada héroe a la función definir_iniciales_nombre.
# En caso que la función definir_iniciales_nombre() retorne False entonces se deberá detener la iteración e informar por pantalla el siguiente mensaje:
#  ‘El origen de datos no contiene el formato correcto’ 
# La función deberá devolver True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error















def stark_imprimir_nombres_con_iniciales():
    '''
    '''
#------------------------------------------------1.3------------------------------------------------------------------
# 1.3- Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
# lista_heroes: la lista de personajes
# La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle las iniciales a los diccionarios contenidos en la lista_heroes
# Luego deberá imprimir la lista completa de los nombres de los personajes seguido de las iniciales encerradas entre paréntesis () 
# 	Se deberá validar:
# Que lista_heroes sea del tipo lista
# Que la lista contenga al menos un elemento
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de viñeta) seguido de un espacio.
# Ejemplo de salida:
# * Howard the Duck (H.D.)
# * Rocket Raccoon (R.R.)
# …
# La función no retorna nada
