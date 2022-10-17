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

    Devueclve el maximo de la lista
    '''
    maximo = lista_personajes[0]

    for personaje in lista_personajes:
        if(personaje[key] > maximo[key]):
            maximo = personaje
    
#----------------------------------------------4.1----------------------------------------------------------------------


#4.1-  Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto.
# Ejemplo de llamada:
# 	calcular_max(lista, 'edad')

















def menu():
    print()

    respuesta = input()

    if(respuesta == "1"):
        pass
    elif(respuesta == "2"):
        pass

