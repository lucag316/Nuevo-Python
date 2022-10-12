import re

def calcula_maximo_minimo(lista:list,clave:str,tipo:str) -> dict:
    '''
    Calcula el maximo/minimo en base a la clave recibida
    
    Recibe una lista de diccionarios, la clave que se utilizara para calcular
    y el tipo de calculo a realizar ("maximo" o "minimo")
    
    Retorna el diccionario que contienen el maximo/minimo o -1 en caso de error
    '''
    retorno = -1
    if(type(lista) == type(list()) and type(clave) == type(str()) and len(lista) > 0):
        max_min = lista[0]
        for video in lista:
            if(tipo == "maximo" and (video[clave] > max_min[clave])):
                max_min = video
            if(tipo == "minimo" and (video[clave] < max_min[clave])):
                max_min = video
        retorno = max_min
    
    return retorno

def calcular_tema_mas_visto(lista:list):
    #---------TEMA MAS VISTO----------------
    video = calcula_maximo_minimo(lista,"views","maximo")
    mostrar_video(video)
    #-------------------------------------------

def calcular_tema_menos_visto(lista:list):
    #---------TEMA MENOS VISTO----------------
    video = calcula_maximo_minimo(lista,"views","minimo")
    mostrar_video(video)
    #-------------------------------------------  
def calcular_tema_mas_largo(lista:list):
    #--------- TEMA MAS LARGO ----------------
    video = calcula_maximo_minimo(lista,"length","maximo")
    mostrar_video(video)
    #-------------------------------------------
def calcular_tema_mas_corto(lista:list):
    #--------- TEMA MAS CORTO ----------------
    video = calcula_maximo_minimo(lista,"length","minimo")
    mostrar_video(video)
    #-------------------------------------------

def calcular_promedio_tiempo(lista:list):
    # -------- PROMEDIO TIEMPO ------------
    acumulador_tiempo_videos = 0
    for tema in lista:
        acumulador_tiempo_videos = acumulador_tiempo_videos +  tema["length"]

    print("Promedio: {2} - QTY: {0} - ACUM: {1} ".format(len(lista),acumulador_tiempo_videos, acumulador_tiempo_videos/len(lista)))

def calcular_promedio_vistas(lista:list):
    # -------- PROMEDIO VISTAS ------------
    acumulador_vistas_videos = 0
    for tema in lista:
        acumulador_vistas_videos +=  tema["views"]

    print("Promedio: {0:.2f} millones".format((acumulador_vistas_videos/len(lista))/1000000))

def mostrar_video(video:dict):

    nuevo_titulo =  transformar_titulo(video["title"])
    nueva_fecha = transformar_fecha_carga(video["date"])
    if(nuevo_titulo["tipo"] != "NO SESSIONS"):
        mensaje = \
        '''
        Tipo : {0}
        Artista: {1}
        Número:  {2}
        Reproducciones: {3} 
        Duración: {4} minutos 
        Código: {5}
        Fecha de farga: {6}
        Hora de carga: {7}
        '''
        print(mensaje.format(   nuevo_titulo["tipo"],
                                nuevo_titulo["artista"],
                                nuevo_titulo["numero"],
                                video["views"]/1000000,
                                video["length"],
                                video["url"][-11:],
                                nueva_fecha["fecha"],
                                nueva_fecha["hora"]))
    else:
        mensaje = \
        '''
        Titulo: {0}
        Reproducciones: {1} 
        Duración: {2} minutos 
        Código: {3}
        Fecha de farga: {4}
        Hora de carga: {5}
        '''
        print(mensaje.format(   video["title"],
                                video["views"]/1000000,
                                video["length"],
                                video["url"][-11:],
                                nueva_fecha["fecha"],
                                nueva_fecha["hora"]))

def transformar_fecha_carga(date:str)->dict:
    '''
    Transforma un str con el formato     
        2022-07-06 00:00:00
    en un diccionario
    {   
        "fecha" : "6/7/2022"
        "hora" : "00:00:00"
    } 
    '''
    lista_rta = re.findall("([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})",date)
    anio,mes,dia,horas,minutos,segundos=lista_rta[0]
    dict_date = {}
    dict_date["fecha"] = "{0}/{1}/{2}".format(dia,mes,anio)
    dict_date["hora"] =  "{0}:{1}:{2}".format(horas,minutos,segundos)
    return dict_date
                
    
def transformar_titulo(titulo:str) -> dict:
    '''
    Si es una session tiene la siguiente forma
        ['QUEVEDO', '||', 'BZRP', 'Music', 'Sessions', '#52']
    => puedo armar el diccionario
            {   
                "tipo" : "BZRP MUSIC SESSIONS"
                "artista" : "Quevedo"
                "numero" :  52
            }
    Sino es un session
    => retornara el diccionario 
            {   
                "tipo" : "NO SESSIONS"
            }
    '''
    retorno={}
    lista_titulo = re.split("[\|#]+",titulo)
    if(len(lista_titulo)==3):
        #Si entro es un titulo de session
        retorno["tipo"] = lista_titulo[1].strip()
        retorno["artista"] = lista_titulo[0].strip()
        retorno["numero"] = lista_titulo[2].strip()
    else:
        retorno["tipo"] = "NO SESSIONS"
    
    return retorno


            