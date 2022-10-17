def buscar_max_min_indice(lista_personajes:list, clave:str, tipo:str)->int:
    '''
    Busca el maximo o minimo, segun el usuario quiera

    Recibe la lista, una clave, y el tipo (maximo o minimo)

    Retorna un entero
    '''
    max_min = 0

    for indice in range(len(lista_personajes)):
        
        if(tipo == "maximo" and lista_personajes[indice][clave] > lista_personajes[max_min][clave]):
            max_min = indice

        elif(tipo == "minimo" and lista_personajes[indice][clave] < lista_personajes[max_min][clave]):
                max_min = indice

    return max_min


def calcula_maximo_minimo(lista:list, clave:str, tipo:str) -> dict:
    """
    Calcula el maximo o el minimo en base a la  clave recibida

    Recibe una lista de diccionarios y la clave que se utilizara para calcular y 
    el tipo de calculo a realizar

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
