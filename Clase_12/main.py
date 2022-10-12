'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("PP_STARWARS/data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
        elif(respuesta=="6"):
            break


starwars_app()

