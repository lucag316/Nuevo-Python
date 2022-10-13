# Ejercicio Integrador 02

# La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
# Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
# preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
# 1- PESO: (entre 10 y 100 kilos)
# 2- PRECIO POR KILO: (mayor a 0 [cero]).
# 3- TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
# A- El importe total a pagar, BRUTO sin descuento.
# B- El importe total a pagar con descuento (Solo si corresponde).
# C- Informar el tipo de alimento más caro.
# D- El promedio de precio por kilo en total.

respuesta = "si"

total_kilos = 0
acumulador_precios = 0
cantidad_productos = 0

alimento_mas_caro = 0
flag_alimento_mas_caro = False
tipo_alimento_mas_caro = ""

precio_total = 0

while(respuesta == "si"):

    peso = float(input("Ingrese el peso  (entre 10 y 100 kilos):  "))
    while(peso < 10 or peso > 100):
        peso = float(input("ERROR, vuelva a ingresar el peso  (entre 10 y 100 kilos):  "))

    precio_por_kilo = int(input("ingrese el precio por kilo:  "))
    while(precio_por_kilo < 0):
        precio_por_kilo = int(input("ERROR, vuelva a ingresar el precio por kilo:  "))
    
    tipo = input("Ingrese el tipo (v, a, m);(vegetal, animal, mezcla):  ")
    while(tipo != "v" and tipo != "a" and tipo != "m"):
        tipo = input("ERROR, vuelva a ingresar el tipo (v, a, m);(vegetal, animal, mezcla):  ")

    if(precio_por_kilo > alimento_mas_caro or flag_alimento_mas_caro == False):
        alimento_mas_caro = precio_por_kilo
        tipo_alimento_mas_caro = tipo
        flag_alimento_mas_caro = True

    total_kilos += peso
    acumulador_precios += precio_por_kilo
    cantidad_productos += 1
    precio_total = precio_por_kilo * total_kilos
    respuesta = input("para CONTINUAR (si)\npara FINALIZAR (otra tecla):  ")

    

if(total_kilos > 100 and total_kilos < 300):
    precio_con_descuento = precio_total * 0.85
    print("El importe total a pagar con descuento es: {0}".format(precio_con_descuento))
    
elif(total_kilos > 300):
    precio_con_descuento = precio_total * 0.75
    print("El importe total a pagar con descuento es: {0}".format(precio_con_descuento))
    
promedio = acumulador_precios / cantidad_productos

print("El importe total a pagar en bruto es: {0}".format(precio_total))

print("El tipo de alimento mas caro es: {0}".format(tipo_alimento_mas_caro))
print("El promedio de precio por kilo es: {0}".format(promedio))