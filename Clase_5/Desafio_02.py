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
def stark_normalizar_datos(lista_personajes:list, clave:str):
    '''
    Normaliza los datos en base a la clave recibida

    Recibe una lista de diccionarios

    Devuelve los datos normalizados en su tipo correspondiente
    '''

    flag_datos_normalizados = False

    for  personaje in lista_personajes:

        if(clave == "altura" or clave == "peso"):

            if(type(personaje[clave]) != type(float())):
                personaje[clave] = float(personaje[clave])
                flag_datos_normalizados = True

        if(clave == "fuerza"):
            if(type(personaje[clave]) != type(int())):
                personaje[clave] == int(personaje[clave])
                flag_datos_normalizados = True

    if(flag_datos_normalizados == True):
        print("Datos  normalizados")

    if(len(lista_personajes)  == 0):
        print("ERROR, lista de heroes vacia")
#----------------------------------------------0-------------------------------------------------------------------------


def obtener_nombre(personaje:dict)->str:
    '''
    Recibe por parametro a un personaje
    
    Devuelve un string con su nombre formateado
    '''
    mensaje = "Nombre: {0}".format(personaje["nombre"])

    return mensaje
#---------------------------------------------1.1------------------------------------------------------------------------

def imprimir_dato(string:str):
    '''
    Recibe por parametro un string y lo imprime por consola
    '''
    print(string)
#---------------------------------------------1.2------------------------------------------------------------------------

def stark_imprimir_nombres_heroes(lista_personajes:list):
    '''
    Recibe la lista de personajes y la imprime por consola, reutiliza las funciones de los puntos 1.1 y 1.2

    Si la lista esta vacia retorna un -1
    '''
    if(len(lista_personajes) > 0):
        for personaje in lista_personajes:

            nombre_personaje = obtener_nombre(personaje)
            imprimir_dato(nombre_personaje)
    else:
        return imprimir_dato("-1")
#----------------------------------------------1.3-----------------------------------------------------------------------

def obtener_nombre_y_dato(personaje:dict, key:str):
    '''
    Recibe al personaje(diccionario) y el dato que desea obtener

    Devuelve el nombre y el dato que desea obtener
    '''
    mensaje = print("Nombre: {0} | {1}: {2}".format(personaje["nombre"], key, personaje[key]))

    return mensaje
#----------------------------------------------2-----------------------------------------------------------------------
#obtener_nombre_y_dato(lista_personajes[0], "altura")

def stark_imprimir_nombres_alturas(lista_personajes:list):
    '''
    Recibe la lista de personajes

    Imprime el nombre y la altura de los personajes

    '''
    if(len(lista_personajes) > 0):

        for personaje in lista_personajes:
            retono = obtener_nombre_y_dato(personaje, "altura")
    else:
        retono = print(-1)

    return retono
#----------------------------------------------3-----------------------------------------------------------------------
#stark_imprimir_nombres_alturas(lista_personajes)
def calcular_max(lista_personajes:list, key:str):
    '''
    Calcula el maximo de la lista  segun la clave elegida

    Recibe la lista de personajes y una key

    Devuelve el maximo de la lista
    '''
    if(type(lista_personajes) == type(list()) and type(key) != type(float())):
        maximo = lista_personajes[0]

        for personaje in lista_personajes:
            if(float(personaje[key]) > float(maximo[key])):
                maximo = personaje
        return maximo
#----------------------------------------------4.1----------------------------------------------------------------------
def calcular_min(lista_personajes:list, key:str):
    '''
    Calcula el minimo de la lista  segun la clave elegida

    Recibe la lista de personajes y una key

    Devuelve el minimo de la lista
    '''
    if(type(lista_personajes) == type(list()) and type(key) != type(float())):
        minimo = lista_personajes[0]

        for personaje in lista_personajes:
            if(float(personaje[key]) < float(minimo[key])):
                minimo = personaje
        return minimo
#----------------------------------------------4.2----------------------------------------------------------------------
def calcular_max_min_dato(lista_personajes:list, clave:str, tipo:str):
    '''
    calcula el maximo o el minimo segun la clave y el tipo que desea calcular, reutiliza las funciones 4.1 y 4.2

    Recibe por parametro la lista de heroes, la clave que desea calcular y el tipo de calculo a realizar(maximo o minimo)

    Retorna al heroe que cumpple con la condicion pedida
    '''
    if(tipo == "maximo"):
        retorno = calcular_max(lista_personajes, clave)
    else:
        retorno = calcular_min(lista_personajes, clave)

    return retorno
#----------------------------------------------4.3----------------------------------------------------------------------

def stark_calcular_imprimir_heroe():
    '''
    '''
#----------------------------------------------4.4----------------------------------------------------------------------

#4.4- Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: 
# La lista de héroes
# El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
# Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3 
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Ejemplo de llamada:
#  	stark_calcular_imprimir_heroe (lista, "maximo", "edad")
#             Ejemplo de salida:
# 	Mayor altura: Nombre: Howard the Duck | altura: 79.34



def menu():
    print()

    respuesta = input()

    if(respuesta == "1"):
        pass
    elif(respuesta == "2"):
        pass

