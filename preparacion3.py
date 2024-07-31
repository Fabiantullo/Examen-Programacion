# El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
# Desea ingresar en el sistema las ventas realizadas en el dia de la fecha y conocer 
# ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que el decida.

# Nombre de carta
# Precio (no puede ser menor a 0)
# Tipo (Magica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

# A) Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000
# B) El nombre y tipo de la carta con menor precio de la rareza Rara.
# C) El porcentaje de rara, super rara y ultra rara hay sobre el total
# [ej: 30% rara ,30% super rara, 40% ultra rara ( debe sumar 100)]
# D) Determinar el precio promedio por cada tipo de carta
# E) Determinar cual fue el tipo de carta mas vendida

seguir = "si"
contador = 0
contador_rara = 0
contador_super_rara = 0
contador_ultra_rara = 0
contador_magica = 0
contador_monstruo = 0
contador_trampa = 0
acumulador_precio_magica = 0
acumulador_precio_monstruo = 0
acumulador_precio_trampa = 0
cantidad_ultra_raras_50000_80000 = 0
bandera_rara = 0
precio_carta_menor_precio_rara = 0

while seguir == "si":
    nombre_carta_ingresada = input("Ingrese el nombre de su carta:  ")
    
    precio_carta_ingresada = int(input("Ingrese el precio de su carta (no menor a 0):  "))
    while precio_carta_ingresada < 0:
        precio_carta_ingresada = int(input("REIngrese el precio de su carta (no menor a 0):  "))

    tipo_carta_ingresada = input("Ingrese el tipo de su carta (Magica, Monstruo o Trampa):  ")
    while tipo_carta_ingresada != "Magica" and tipo_carta_ingresada != "Monstruo" and tipo_carta_ingresada != "Trampa":
        tipo_carta_ingresada = input("REIngrese el tipo de su carta (Magica, Monstruo o Trampa):  ")
    
    rareza_carta_ingresada = input("Ingrese la rareza de su carta (Rara, Super Rara o Ultra Rara):  ")
    while rareza_carta_ingresada != "Rara" and rareza_carta_ingresada != "Super Rara" and rareza_carta_ingresada != "Ultra Rara":
        rareza_carta_ingresada = input("REIngrese la rareza de su carta (Rara, Super Rara o Ultra Rara):  ")

    match rareza_carta_ingresada:
        case "Ultra Rara":
            if precio_carta_ingresada > 50000 and precio_carta_ingresada < 80000:
                cantidad_ultra_raras_50000_80000 += 1
            contador_ultra_rara += 1
            
        case "Rara":
            if bandera_rara == 0:
                nombre_carta_menor_precio_rara = nombre_carta_ingresada
                tipo_carta_menor_precio_rara = tipo_carta_ingresada
                precio_carta_menor_precio_rara = precio_carta_ingresada

            elif precio_carta_menor_precio_rara > precio_carta_ingresada:
                nombre_carta_menor_precio_rara = nombre_carta_ingresada
                tipo_carta_menor_precio_rara = tipo_carta_ingresada
                precio_carta_menor_precio_rara = precio_carta_ingresada
            contador_rara += 1

        case _ :
            contador_super_rara += 1

    match tipo_carta_ingresada:
        case "Magica":
            acumulador_precio_magica += precio_carta_ingresada
            contador_magica += 1
        
        case "Monstruo":
            acumulador_precio_monstruo += precio_carta_ingresada
            contador_monstruo += 1
        
        case _ :
            acumulador_precio_trampa += precio_carta_ingresada
            contador_trampa += 1
    contador += 1
    seguir = input("¿Quiere seguir? si/no:  ")

# A) Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000
# B) El nombre y tipo de la carta con menor precio de la rareza Rara.
# C) El porcentaje de rara, super rara y ultra rara hay sobre el total
# [ej: 30% rara ,30% super rara, 40% ultra rara ( debe sumar 100)]
# D) Determinar el precio promedio por cada tipo de carta
# E) Determinar cual fue el tipo de carta mas vendida
porcentaje_rara = (contador_rara / contador) * 100
porcentaje_super_rara = (contador_super_rara / contador) * 100
porcentaje_ultra_rara = (contador_ultra_rara / contador) * 100

promedio_magica = acumulador_precio_magica / contador_magica
promedio_monstruo = acumulador_precio_monstruo / contador_monstruo
promedio_trampa = acumulador_precio_trampa / contador_trampa

print(f"La cantidad de cartas de rareza Ultra rara cuyo precio oscila entre 50000 y 80000 es:  {cantidad_ultra_raras_50000_80000}")
print(f"La carta con menor precio de rareza rara es:\nNombre: {nombre_carta_menor_precio_rara}\nTipo: {tipo_carta_menor_precio_rara}")
print(f"El porcentaje de cartas es: Raras {porcentaje_rara:.2f}% Super Raras {porcentaje_super_rara:.2f}% y Ultra Raras {porcentaje_ultra_rara:.2f}%")
print(f"El precio promedio de cada tipo de carta es: Magica {promedio_magica} Monstruo {promedio_monstruo} y Trampa {promedio_trampa}")