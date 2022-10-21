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
    i = 0

    if(len(lista_heroes) > 0):

        for heroe in lista_heroes:

            if(type(heroe) == type(dict())):

                i += 1
                agregar_codigo_heroe(heroe, i)
                
                print("El código del héroe es: {0}".format(heroe["codigo_heroe"]))

        print("Se asignaron {0} códigos".format(i))

    else:
        print("El origen de datos no contiene el formato correcto")
#------------------------------------------------2.3------------------------------------------------------------------
#stark_generar_codigos_heroes(lista_personajes)
#FALTA VALIDAR QUE TODOS LOS ELEMENTOS TENGAN LA CLAVE GENERO

def sanitizar_entero(numero_str:str):
    '''
    La funcion analiza si es un numero entero positivo

    Recibe un numero tipo string que representa un posible numero entero

    si contiene caracteres no numericos retorna un -1, si el numero es negativo retorna un -2, si ocurren otros errores que no permiten convertirlo a entero retorna un -3, si es un numero entero positivo lo retorna convertido a entero
    '''
    encontrar_no_numericos = re.findall("[a-zA-Z]+", numero_str)
    
    retorno = -1

    if(len(encontrar_no_numericos) == 0):

        encontrar_numero = re.findall("^[+-]?[0-9]+$", numero_str)
        numero_str = numero_str.strip()

        
        if(len(encontrar_numero) == 1):
            numero_int = int(numero_str)

            if(type(numero_int) == type(int())):
                
                if(numero_int > 0):
                    retorno = numero_int

                else:
                    retorno = -2

        else:
            retorno = -3

    return retorno
#------------------------------------------------3.1------------------------------------------------------------------
#print(sanitizar_entero("468"))

def sanitizar_flotante(numero_str:str):
    '''
    La funcion analiza si es un flotante positivo

    Recibe un numero tipo string que representa un posible numero decimal

    si contiene caracteres no numericos retorna un -1, si el numero es negativo retorna un -2, si ocurren otros errores que no permiten convertirlo a entero retorna un -3, si es un numero entero positivo lo retorna convertido a flotante
    '''
    encontrar_no_numericos = re.findall("[a-zA-Z]+", numero_str)
    
    retorno = -1

    if(len(encontrar_no_numericos) == 0):

        encontrar_numero = re.findall("^[+-]?[0-9]+$", numero_str)
        numero_str = numero_str.strip()

        
        if(len(encontrar_numero) == 1):
            numero_float = float(numero_str)

            if(type(numero_float) == type(float())):
                
                if(numero_float > 0):
                    retorno = numero_float

                else:
                    retorno = -2

        else:
            retorno = -3

    return retorno
#------------------------------------------------3.2------------------------------------------------------------------
#print(sanitizar_entero("468"))
#NO SE SI ESTA BIEN (NO SE SI TIENE QUE PODER ACEPTAR PUNTOS O COMAS, POR SI ES DECIMAL)


def sanitizar_string(valor_str:str, valor_por_defecto:str):
    '''
    La funcion analiza si el  string recibido es solo  texto, en caso de encontrarse números retorna “N/A”

    Recibe un string que representa el texto a validar, un string que representa un valor por defecto (parámetro opcional, inicializarlo con ‘-’)

    En caso que el parámetro recibido sea solo texto retorna el mismo convertido todo a minúsculas, en caso
    '''
#------------------------------------------------3.3------------------------------------------------------------------

# 3.3- Crear la función ‘sanitizar_string’ la cual recibirá como parámetro
# valor_str: un string que representa el texto a validar
# valor_por_defecto: un string que representa un valor por defecto (parámetro opcional, inicializarlo con ‘-’)
# La función deberá analizar el string recibido y determinar si es solo texto (sin números). En caso de encontrarse números retornar “N/A”
# En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un espacio
# 	El espacio es un caracter válido 
# En caso que se verifique que el parámetro recibido es solo texto, se deberá retornar el mismo convertido todo a minúsculas
# En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor por defecto, entonces retornar el valor por defecto convertido a minúsculas
# Quitar los espacios en blanco de atras y adelante de ambos parámetros en caso que los tuviese






