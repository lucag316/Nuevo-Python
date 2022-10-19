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

        nombre_heroe = nombre_heroe.strip()
        nombre_heroe = nombre_heroe.split(" ")
        partes_nombre = nombre_heroe

        for parte in partes_nombre:
            iniciales += parte[0] + "."

        retorno = iniciales
    
    return retorno
#------------------------------------------------1.1------------------------------------------------------------------

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
#print(definir_iniciales_nombre(lista_personajes[0]))

#FALTA VALIDAR QUE EL DICCIONARIO CONTENGA  LA  CLAVE NOMBRE

def agregar_iniciales_nombre(lista_heroes:list):
    '''
    Itera la  lista de personajes  pasandole a cada uno la funcion "definir_iniciales_nombre",si la funcion retorna False, imprime: ‘El origen de datos no contiene el formato correcto’ 

    Recibe por parametro la lista de personajes

    La función devuelve True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error
    '''
    if(type(lista_heroes) == type(list()) and len(lista_heroes) > 0):

        for heroe in lista_heroes:

            if(definir_iniciales_nombre(heroe) == False):
                print("El origen de datos no contiene el formato correcto")
                retorno = False
            else:
                retorno = True

        return retorno
#------------------------------------------------1.3------------------------------------------------------------------
#print(agregar_iniciales_nombre(lista_personajes))

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    '''
    Utiliza la  funcion 'agregar_iniciales_nombre' para añadir las iniciales a los diccionarios

    Recibe la lista de personajes

    imprime la lista completa de los nombres de los personajes seguido de las iniciales encerradas entre paréntesis () 
    '''
    if(type(lista_heroes) == type(list()) and len(lista_heroes) > 0):
        agregar_iniciales_nombre(lista_heroes)

        for heroe in lista_heroes:
            print("* {0} ({1})".format(heroe["nombre"], heroe["iniciales"]))
#------------------------------------------------1.3------------------------------------------------------------------
#stark_imprimir_nombres_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    '''
    La funcion genera un string con este formato GENERO-000…000ID

    Recibe por parametro el id_heroe(entero que repersenta al identificador del personaje), el genero_heroe(un string "M", "F"  o "NB")

    En caso de no pasar las validaciones retorna "N/A", sino retorna el codigo generado
    '''
    if(type(id_heroe) == type(int()) and genero_heroe != ""):

        if(genero_heroe != "M" and genero_heroe != "F" and genero_heroe != "NB"):
            retorno = "N/A"

        else:
            relleno = 10 - (len(genero_heroe) + 1)
            id_nuevo_str = str(id_heroe).zfill(relleno)
            retorno = "{0}-{1}".format(genero_heroe, id_nuevo_str)

    return retorno
#------------------------------------------------2.1------------------------------------------------------------------
#print(generar_codigo_heroe(555, "NB"))

def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    '''
    La funcion agrega una nueva clave llamada ‘codigo_heroe’ al diccionario del personaje, le asigna como valor un codigo utilizando la funcion  ‘generar_codigo_heroe’

    Recibe al diccionario del personaje, el id_heroe: un entero que representa el identificador del héroe

    Retorna True, en caso de encontrar algun error retorna False
    '''
    
    retorno = False

    codigo_recibido = generar_codigo_heroe(id_heroe, heroe["genero"])

    if(heroe != "" and len(codigo_recibido) == 10):

        heroe["codigo_heroe"] = codigo_recibido
        retorno = True

    return retorno
#------------------------------------------------2.2------------------------------------------------------------------
#print(agregar_codigo_heroe(lista_personajes[0], 5555))

def stark_generar_codigos_heroes(lista_heroes:list):
    '''
    Itera la lista y le agrega el codigo_heroe a cada personaje, reutiliza la funcion agregar_codigo_heroe, le pasa como argumento el personaje que se esta iterando y el id_heroe

    Recibe la lista de personajes

    Imprime por pantalla, ejemplo: (El código del primer héroe es: M-00000001), en caso de encontrar algun error informa por pantalla ‘El origen de datos no contiene el formato correcto’
    '''
    i = 1
    if(len(lista_heroes) > 0):

        for heroe in lista_heroes:

            if(type(heroe) == type(dict())):

                agregar_codigo_heroe(heroe, i)
                i += 1

                print("El código del primer héroe es: {0}".format(heroe["codigo_heroe"]))

#------------------------------------------------2.3------------------------------------------------------------------
stark_generar_codigos_heroes(lista_personajes)


# Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
# (## representa la cantidad de códigos generados):
# Se asignaron ## códigos 
# *   El código del primer héroe es: 		M-00000001
# * El código del del último héroe es: 	M-00001224


# Todos los elementos de la lista sean del tipo diccionario
# Todos los elementos contengan la clave ‘genero’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no contiene el formato correcto’
# 	La función no retorna ningún valor.

