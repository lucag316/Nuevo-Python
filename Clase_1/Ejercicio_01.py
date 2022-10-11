# Ejercicio Integrador 01

# La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:

# 1- El tipo (validar "barbijo", "jabón" o "alcohol")
# 2- El precio: (validar entre 100 y 300)
# 3- La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
# 4- La marca y el Fabricante.
  
#  Se debe informar lo siguiente:
# A- Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B- Del ítem con más unidades, el fabricante.
# C- Cuántas unidades de jabones hay en total.


barbijo_mas_caro = 0
flag_barbijo_mas_caro = False
barbijo_mas_caro_unidades = 0
barbijo_mas_caro_fabricante = ""

item_mas_unidades = 0
flag_item_mas_unidades = False
fabricante_mas_unidades = ""

cantidad_jabones = 0

for producto in range(5):

    tipo = input("Ingrese el tipo del producto (barbijo), (jabon), (alcohol):  ")
    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("ERROR, vuelva a ingresar el tipo (barbijo), (jabon), (alcohol):  ")

    precio = int(input("Ingrese el precio (entre 100 y 300):  "))
    while(precio < 100 or precio > 300):
        precio = int(input("ERROR, vuelva a ingresar el precio (entre 100 y 300):  "))

    unidades = int(input("ingrese la cantidad de unidades (entre 1 y 1000):  "))
    while(unidades < 1 or unidades > 1000):
        unidades = int(input("ERROR, vuelva a ingresar la cantidad de unidades (entre 1 y 1000):  "))

    marca = input("Ingrese la  marca:  ")
    fabricante = input("Ingrese el  fabricante:  ")

    if(tipo == "barbijo"):
        if(precio > barbijo_mas_caro or flag_barbijo_mas_caro == False):
            barbijo_mas_caro = precio
            barbijo_mas_caro_unidades = unidades
            barbijo_mas_caro_fabricante = fabricante
            flag_barbijo_mas_caro = True

    if(unidades > item_mas_unidades or flag_item_mas_unidades == False):
        item_mas_unidades = unidades
        flag_item_mas_unidades = True
        fabricante_mas_unidades = fabricante
    
    if(tipo == "jabon"):
        cantidad_jabones += 1

print("Cantidad de unidades del barbijo mas caro: {0}  y su fabricante es: {1}".format(barbijo_mas_caro_unidades, barbijo_mas_caro_fabricante))
print("El fabricante con mas unidades es: {0}".format(fabricante_mas_unidades))
print("La cantidad de jabones es: {0}".format(cantidad_jabones))