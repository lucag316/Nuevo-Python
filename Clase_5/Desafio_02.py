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

def stark_calcular_imprimir_heroe(lista_personajes:list, key:str, tipo:str):
    '''
    Reutiliza las funciones 1.2, 2 y 4.3, calcula al personaje segun lo pedido y muestra su nombre y la clave calculada

    Recibe por parametros, la lista de personajes, la clave del dato a calcular, y el tipo de calculo(maximo o minimo)

    obtiene al personaje que cumple con las condiciones, Imprime el nombre del personaje y el valor calculado
    '''
    if(len(lista_personajes) > 0):
        datos_personaje = calcular_max_min_dato(lista_personajes, key, tipo)
        datos_personaje = obtener_nombre_y_dato(datos_personaje, key)
        
    else:
        datos_personaje = -1

    imprimir_dato(datos_personaje)
#----------------------------------------------4.4----------------------------------------------------------------------

def sumar_dato_heroe(lista_personajes:list, key:str):
    '''
    Suma  segun la clave que desea 

    Recibe la lista de personajes y una clave

    Retorna la suma completa de todo los personajes segun la clave que ingrese
    '''
    suma = 0

    for personaje in lista_personajes:
        if(type(personaje) != type(dict()) or personaje == ""):
            suma = -1
        else:
            suma += float(personaje[key])

    return suma
#----------------------------------------------5.1----------------------------------------------------------------------

def dividir(dividendo:int, divisor:int) -> float:
    '''
    Realiza la division entre los dos parametros

    Recibe 2 parametros tipo int(dividendo y divisor)

    Retorna la division hecha, en caso de que el divisor sea 0 retorna un 0
    '''
    if(divisor == 0):
        division = 0
    else: 
        division = dividendo / divisor
    
    return division
#----------------------------------------------5.2----------------------------------------------------------------------
def calcular_promedio(lista_personajes:list, key:str):
    '''
    Calcula el promedio segun el dato pasado, reutiliza las funciones 5.1 y 5.2

    Recibe la lista de personajes y la clave que se requiere calcular el promedio

    Retorna el promedio del dato pasado por parametro
    '''
    cantidad_personajes = len(lista_personajes) 
    suma = sumar_dato_heroe(lista_personajes,  key)
    
    promedio = dividir(suma, cantidad_personajes)

    return promedio
#----------------------------------------------5.3----------------------------------------------------------------------
def stark_calcular_imprimir_promedio_altura(lista_personajes:list):
    '''
    Calcula la altura promedio, reutiliza las funciones 1.2 y 5.3

    Recibe por parametro la lista de personajes

    Imprime la altura promedio
    '''
    if(lista_personajes == ""):
        promedio_altura = -1
    else:
        promedio_altura = calcular_promedio(lista_personajes, "altura")

    imprimir_dato(promedio_altura)
#----------------------------------------------5.4----------------------------------------------------------------------

def imprimir_menu():
    '''
    Imprime el menu de opciones, reutiliza la funcion 1.2
    '''

    while True:

        print("1- Imprimir nombres de los personajes \n2- Imprimir nombre y alturas \n3- Calcular heroe segun su clave y tipo de calculo \n4- Calcular promedio segun la  clave \n5- Promedio altura   \n6- Salir")

        respuesta = input()

        if(respuesta == "1"):
            stark_imprimir_nombres_heroes(lista_personajes)
        elif(respuesta == "2"):
            stark_imprimir_nombres_alturas(lista_personajes)
        elif(respuesta == "3"):

            key = input("Ingrese la clave que desea calcular (altura, peso,  fuerza):  ")
            while(key  != "altura" and key != "peso" and key != "fuerza"):
                key = input("ERROR, reingrese la clave que desea calcular (altura, peso,  fuerza):  ")

            tipo = input("Ingrese el tipo de calculo(maximo o minimo):  ")
            while(tipo != "maximo" and  tipo != "minimo"):
                tipo = input("ERROR, reingrese el tipo de calculo(maximo o minimo):  ")

            stark_calcular_imprimir_heroe(lista_personajes, key, tipo)
        elif(respuesta == "4"):

            key = input("Ingrese la clave que desea calcular (altura, peso,  fuerza):  ")
            while(key  != "altura" and key != "peso" and key != "fuerza"):
                key = input("ERROR, reingrese la clave que desea calcular (altura, peso,  fuerza):  ")

            calcular_promedio(lista_personajes, key)
        elif(respuesta == "5"):
            stark_calcular_imprimir_promedio_altura(lista_personajes)
        elif(respuesta == "6"):
            break
#----------------------------------------------6.1----------------------------------------------------------------------
imprimir_menu()
# 6.1-  Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)








def validar_entero(numero:str):
    '''
    Recibe como parametro un numero de tipo string, el cual se verifica que este conformado solo por digitos

    Retorna True en caso de serlo, False caso contrario
    '''
    if(type(numero) == type(str())):
        pass
#----------------------------------------------6.2----------------------------------------------------------------------

# 6.2- Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario








def stark_menu_principal():
    '''
    Imprime el  menu de opciones
    '''
#----------------------------------------------6.3----------------------------------------------------------------------

# 6.3- Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2




def stark_marvel_app():
    '''
    '''
#----------------------------------------------7----------------------------------------------------------------------

# 7- Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.























#EN EL 5.4 NO SE COMO USAR LA  FUNCION 5.1 (ESTA HECHO PERO SIN REUTILIZAR LA OTRA FUNCION)