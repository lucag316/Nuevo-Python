# Ejercicio Integrador 03

# La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
# 1- Nombre de Heroína/Héroe
# 2- EDAD (mayores a 18 años)
# 3- Sexo ("m", "f" o "nb")
# 4- Habilidad ("fuerza", "magia", "inteligencia").
# A su vez, el programa deberá mostrar por consola lo siguiente:
# A- Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
# B- El sexo y nombre de Heroe | Heroína de mayor edad.
# C- La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
# D- El promedio de edad entre Heroinas.
# E- El promedio de edad entre Heroes de fuerza.


respuesta = "si"

edad_fuerza_mas_joven = 999999999999999999999999999999999999999
flag_edad_fuerza_mas_joven = False

edad_mayor = 0
flag_edad_mayor = False

cantidad_heroinas_habilidades = 0

cantidad_heroinas = 0
acumulador_edad_heroinas = 0

cantidad_heroes_fuerza = 0
acumulador_edad_heroes_fuerza = 0

while(respuesta == "si"):

    nombre = input("Ingrese el nombre del personaje:  ")
    while(nombre == ""):
        nombre = input("ERROR, reingrese el nombre del personaje:  ")

    edad = int(input("Ingrese la edad (mayor a 18):  "))
    while(edad < 18):
        nombre = input("ERROR, reingrese el nombre del personaje:  ")

    sexo = input("Ingrese el sexo (m), (f), (nb):  ")
    while(sexo != "m" and sexo != "f" and sexo != "nb"):
        sexo = input("ERROR, reingrese el sexo (m), (f), (nb):  ")

    habilidad = input("Ingrese la habilidad (fuerza), (magia), (inteligencia):  ")
    while(habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):
        habilidad = input("ERROR, reingrese la habilidad (fuerza), (magia), (inteligencia):  ")


    if(edad > edad_mayor or flag_edad_mayor == False):
        edad_mayor = edad
        nombre_mayor_edad = nombre
        sexo_mayor_edad = sexo
        flag_edad_mayor = True

    if(habilidad == "fuerza"):

        if(edad < edad_fuerza_mas_joven or flag_edad_fuerza_mas_joven == False):
            edad_fuerza_mas_joven_nombre = nombre
            edad_fuerza_mas_joven = edad
            flag_edad_fuerza_mas_joven = True

        if(sexo == "m"):
            cantidad_heroes_fuerza += 1
            acumulador_edad_heroes_fuerza += edad

    if(sexo == "f"):
        cantidad_heroinas += 1
        acumulador_edad_heroinas += edad

        if(habilidad == "fuerza" or habilidad == "magia"):
            cantidad_heroinas_habilidades += 1

    respuesta = input("para CONTINUAR (si)\npara FINALIZAR (otra tecla):  ")

promedio_heroinas =  acumulador_edad_heroinas / cantidad_heroinas
promedio_heroes = acumulador_edad_heroes_fuerza / cantidad_heroes_fuerza

print("Nombre del personaje de fuerza mas joven:  {0}".format(edad_fuerza_mas_joven_nombre))
print("El nombre del personaje  de mayor edad es: {0} , y su sexo: {1}".format(nombre_mayor_edad, sexo_mayor_edad))
print("La cantidad de heroinas de fuerza/magia es: {0}".format(cantidad_heroinas_habilidades))
print("El promedio de edad entre heroinas es: {0}".format(promedio_heroinas))
print("El promedio de edad entre heroes es: {0}".format(promedio_heroes))

# A- Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
# B- El sexo y nombre de Heroe | Heroína de mayor edad.
# C- La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
# D- El promedio de edad entre Heroinas.
# E- El promedio de edad entre Heroes de fuerza.




#ERROR EN LA LINEA 77