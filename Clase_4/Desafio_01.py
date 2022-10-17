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
from data_stark import lista_personajes

#########################################################################################################################
def normalizar_datos(lista_personajes:list):
    '''
    Normaliza los datos, convierte a la altura y el peso en un tipo float, y a fuerza los convierte en un tipo int

    Recibe la lista de personajes
    '''
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
    '''
    Recibe la lista de personajes, y crea una lista solo con los personajes femeninos

    Devuelve una lista con los personajes femeninos
    '''
    lista_femeninos = []

    for personaje in lista_personajes:

        if(personaje["genero"] == "F"):
            lista_femeninos.append(personaje)

    return lista_femeninos
def crear_lista_masculinos(lista_personajes:list)->list:
    '''
    Recibe la lista de personajes, y crea una lista solo con los personajes masculinos

    Devuelve una lista con los personajes masculinos
    '''
    lista_masculinos = []

    for personaje in lista_personajes:

        if(personaje["genero"] == "M"):
            lista_masculinos.append(personaje)

    return lista_masculinos

lista_femeninos = crear_lista_femeninos(lista_personajes)
lista_masculinos = crear_lista_masculinos(lista_personajes)

def calcula_maximo_minimo(lista:list, clave:str, tipo:str) -> dict:
    """
    Calcula el maximo o el minimo en base a la  clave recibida

    Recibe una lista de diccionarios y la clave que se utilizara para calcular y 
    el tipo (maximo o minimo) de calculo a realizar

    Devuelve/retorna el  diccionario que contiene el maximo o minimo, o [-1] en caso de ERROR
    """
    retorno = -1
    if(type(lista) == type([]) and type(clave) == type("") and len(lista) > 0):
        maximo_minimo = lista[0]

        for personaje in lista:
            if(tipo == "maximo" and float(personaje[clave]) > float(maximo_minimo[clave])):
                maximo_minimo = personaje #te guardas el diccionario entero

            if(tipo == "minimo" and float(personaje[clave]) < float(maximo_minimo[clave])):
                maximo_minimo = personaje #te guardas el diccionario entero

        retorno = maximo_minimo
    return retorno
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

def calcular_masculino_mas_alto(lista_personajes:list):
    '''
    Busca al personaje masculino mas alto y lo retorna

    Recibe la lista de personajes
    '''
    masculino_mas_alto = calcula_maximo_minimo(lista_personajes, "altura", "maximo")

    return masculino_mas_alto
#-----------------------------------------PUNTO C-------------------------------------------------------------------------
def calcular_femenino_mas_alto(lista_personajes:list):
    '''
    Busca al personaje femenino mas alto y lo retorna

    Recibe la lista de personajes
    '''
    femenino_mas_alto = calcula_maximo_minimo(lista_personajes, "altura", "maximo")

    return femenino_mas_alto
#-----------------------------------------PUNTO D-------------------------------------------------------------------------
def calcular_masculino_mas_bajo(lista_personajes:list):
    '''
    Busca al personaje masculino mas bajo y lo retorna

    Recibe la lista de personajes
    '''
    masculino_mas_bajo = calcula_maximo_minimo(lista_personajes, "altura", "minimo")

    return masculino_mas_bajo
#-----------------------------------------PUNTO E-------------------------------------------------------------------------
def calcular_femenino_mas_bajo(lista_personajes:list):
    '''
    Busca al personaje femenino mas bajo y lo retorna

    Recibe la lista de personajes    
    '''
    femenino_mas_bajo = calcula_maximo_minimo(lista_personajes, "altura", "minimo")

    return femenino_mas_bajo
#-----------------------------------------PUNTO F-------------------------------------------------------------------------

def calcular_promedio_altura_masculino(lista_personajes:list):
    '''
    Calcula el promedio de la altura de los personajes masculinos

    Recibe la lista de masculinos
    '''
    acumulador_alturas = 0
    cantidad_masculinos = 0

    for personaje in lista_personajes:
        acumulador_alturas += personaje["altura"]
        cantidad_masculinos += 1

    promedio = acumulador_alturas / cantidad_masculinos
    mensaje = "El promedio de altura masculino es: {0}".format(promedio)

    return mensaje
#-----------------------------------------PUNTO G-------------------------------------------------------------------------
def calcular_promedio_altura_femeninos(lista_personajes:list):
    '''
    Calcula el promedio de la altura de los personajes femeninos

    Recibe la lista de femeninos
    '''
    acumulador_alturas =  0
    cantidad_femeninos = 0

    for personaje in lista_personajes:
        acumulador_alturas += personaje["altura"]
        cantidad_femeninos += 1

    promedio = acumulador_alturas / cantidad_femeninos
    mensaje = "El promedio de altura femenino es: {0}".format(promedio)

    return mensaje
#-----------------------------------------PUNTO H-------------------------------------------------------------------------

def calcular_nombres_de_anteriores_puntos():
    '''
    Obtiene los nombres de los puntos C al F
    '''
    masculino_mas_alto = calcular_masculino_mas_alto(lista_masculinos)
    print("El nombre del masculino mas alto es: {0}" .format(masculino_mas_alto["nombre"]))

    femenino_mas_alto = calcular_femenino_mas_alto(lista_femeninos)
    print("El nombre del femenino mas alto es: {0}" .format(femenino_mas_alto["nombre"]))


    masculino_mas_bajo = calcular_femenino_mas_bajo(lista_masculinos)
    print("El nombre del masculino mas bajo es: {0}" .format(masculino_mas_bajo["nombre"]))

    femenino_mas_bajo = calcular_femenino_mas_bajo(lista_femeninos)
    print("El nombre del femenino mas bajo es: {0}" .format(femenino_mas_bajo["nombre"]))
#-----------------------------------------PUNTO I-------------------------------------------------------------------------

def calcular_tipo_color_ojos(lista_personajes:list):
    '''
    Calcula cuantos personajes son de cada color de ojos

    recibe la lista de personajes
    '''
    tipo_color_ojos = {}
    for personaje in lista_personajes:
        tipo_color_ojos[personaje["color_ojos"]] = 0
        
    for personaje  in lista_personajes:
        tipo_color_ojos[personaje["color_ojos"]] += 1

    print(tipo_color_ojos)
#-----------------------------------------PUNTO J-------------------------------------------------------------------------
def calcular_tipo_color_pelo(lista_personajes:list):
    '''
    Calcula cuantos personajes son de cada color de pelo

    Recibe la lista de personajes
    '''
    tipo_color_pelo = {}
    for personaje in lista_personajes:
        tipo_color_pelo[personaje["color_pelo"]] = 0
        
    for personaje  in lista_personajes:
        tipo_color_pelo[personaje["color_pelo"]] += 1

    print(tipo_color_pelo)
#-----------------------------------------PUNTO K-------------------------------------------------------------------------
def calcular_tipo_inteligencia(lista_personajes:list):
    '''
    Calcula cuantos personajes son  de cada tipo de inteligencia

    Recibe la lista de personajes
    '''
    tipo_inteligencia = {}
    for personaje in lista_personajes:
        if (personaje["inteligencia"] == ""):
            tipo_inteligencia["No tiene"] = 0
        else:   
            tipo_inteligencia[personaje["inteligencia"]] = 0

    for personaje in lista_personajes:
        if (personaje["inteligencia"] == ""):
            tipo_inteligencia["No tiene"] += 1
        else:
            tipo_inteligencia[personaje["inteligencia"]] += 1

    print(tipo_inteligencia)
#-----------------------------------------PUNTO L-------------------------------------------------------------------------

def listar_color_ojos(lista_personajes:list):
    '''
    Agrupa a los personajes por el color de ojos que tienen

    Recibe la lista de personajes
    '''
    dic_color_ojos = {}

    for personaje in lista_personajes:

        personaje["color_ojos"] = personaje["color_ojos"].lower()
        color_ojos = personaje["color_ojos"]
        dic_color_ojos[color_ojos] = []

    for personaje in lista_personajes:
        for color in dic_color_ojos:

            color_ojos = personaje["color_ojos"]
            if (color_ojos == color):
                dic_color_ojos[color].append(personaje["nombre"])
        
    print(dic_color_ojos)
#-----------------------------------------PUNTO M-------------------------------------------------------------------------
def listar_color_pelo(lista_personajes:list):
    '''
    Agrupa a todos los personajes por el color de pelo que tienen

    Recibe la lista de personajes
    '''
    dic_color_pelo = {}

    for personaje in lista_personajes:

        personaje["color_pelo"] = personaje["color_pelo"].lower()
        color_pelo = personaje["color_pelo"]
        dic_color_pelo[color_pelo] = []

    for personaje in lista_personajes:
        for color in dic_color_pelo:

            color_pelo = personaje["color_pelo"]
            if(color_pelo == color):
                dic_color_pelo[color].append(personaje["nombre"])
    
    print(dic_color_pelo)
#-----------------------------------------PUNTO N-------------------------------------------------------------------------
def listar_tipo_inteligencia(lista_personajes:list):
    '''
    Agrupa a todos los personajes segun el tipo de inteligencia que tienen

    Recibe la lista de personajes
    '''
    dic_tipo_inteligencia = {}

    for personaje in lista_personajes:

        personaje["inteligencia"] = personaje["inteligencia"].lower()
        tipo_inteligencia = personaje["inteligencia"]
        dic_tipo_inteligencia[tipo_inteligencia] = []

    for personaje in lista_personajes:
        for tipo in dic_tipo_inteligencia:

            tipo_inteligencia = personaje["inteligencia"]
            if(tipo == tipo_inteligencia):
                dic_tipo_inteligencia[tipo].append(personaje["nombre"])

    print(dic_tipo_inteligencia)
#-----------------------------------------PUNTO O-------------------------------------------------------------------------

def menu():
    while True:
        print("1- Nombres masculinos \n2- Nombres femeninos \n3- Personaje mas alto masculino \n4- Personaje mas alto femenino \n5- Personaje mas bajo masculino \n6- Personaje mas bajo femenino \n7- Altura promedio masculinos \n8- Altura promedio femeninos \n9- Calcular nombres de puntos anteriores \n10- Cantidad de color de ojos de cada tipo \n11- Cantidad de color de pelo de cada tipo \n12- cantidad de inteligencia de cada tipo \n13- Listar personajes por color de ojos \n14- Listar personajes por color de pelo \n15- Listar personajes por tipo de inteligencia \n16- Salir")

        respuesta = input()

        if(respuesta == "1"):
            imprimir_nombres_masculinos(lista_personajes)
        elif(respuesta == "2"):
            imprimir_nombre_femeninos(lista_femeninos)
        elif(respuesta == "3"):
            print(calcular_masculino_mas_alto(lista_masculinos))
        elif(respuesta == "4"):
            print(calcular_femenino_mas_alto(lista_femeninos))
        elif(respuesta == "5"):
            print(calcular_masculino_mas_bajo(lista_masculinos))
        elif(respuesta == "6"):
            print(calcular_femenino_mas_bajo(lista_femeninos))
        elif(respuesta == "7"):
            print(calcular_promedio_altura_masculino(lista_masculinos))
        elif(respuesta == "8"):
            print(calcular_promedio_altura_femeninos(lista_femeninos))
        elif(respuesta == "9"):
            calcular_nombres_de_anteriores_puntos()
        elif(respuesta == "10"):
            calcular_tipo_color_ojos(lista_personajes)
        elif(respuesta == "11"):
            calcular_tipo_color_pelo(lista_personajes)
        elif(respuesta == "12"):
            calcular_tipo_inteligencia(lista_personajes)
        elif(respuesta == "13"):
            print(listar_color_ojos(lista_personajes))
        elif(respuesta == "14"):
            print(listar_color_pelo(lista_personajes))
        elif(respuesta == "15"):
            print(listar_tipo_inteligencia(lista_personajes))
        elif(respuesta == "16"):
            break
        
menu()