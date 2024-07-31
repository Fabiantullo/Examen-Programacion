# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la
#  compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

# Se aplicará el siguiente descuento:
# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de
#  otra marca el descuento es del 20%.
# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % 
# y si es de otra marca un 5%.

# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

# Mostrar por pantalla: 

# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional
#  (si corresponde) y el total a pagar con descuento.

precio_lamparas = 800
descuento = 0
descuento_extra = 0

marca_ingresada = input("Ingrese la marca de lampara (ArgentinaLuz, FelipeLamparas o Generico):  ")
while marca_ingresada != "ArgentinaLuz" and marca_ingresada != "FelipeLamparas" and marca_ingresada != "Generico":
    marca_ingresada = input("REIngrese la marca de lampara (ArgentinaLuz, FelipeLamparas o Generico):  ")

cantidad_lamparas_ingresada = int(input("Ingrese la cantidad de lamparas que desea:  "))

match cantidad_lamparas_ingresada:
    case n if n > 6:
        descuento = 50
    
    case 5:
        match marca_ingresada:
            case "ArgentinaLuz":
                descuento = 40
            case _: 
                descuento = 30

    case 4:
        match marca_ingresada:
            case "ArgentinaLuz" | "FelipeLamparas":
                descuento = 25
            
            case _: 
                descuento = 20

    case 3: 
        match marca_ingresada:
            case "ArgentinaLuz":
                descuento = 15

            case "FelipeLamparas":
                descuento = 10
            
            case _: 
                descuento = 5

total_sin_descuento = precio_lamparas * cantidad_lamparas_ingresada

if total_sin_descuento > 4000:
    descuento_extra = 5

total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento / 100)
total_con_descuento_extra = total_con_descuento - (total_con_descuento * descuento_extra / 100)



# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional
#  (si corresponde) y el total a pagar con descuento.

print(f"La marca es:  {marca_ingresada}")
print(f"La cantidad de lamparas es: {cantidad_lamparas_ingresada}")
print(f"El total sin descuento es de: {total_sin_descuento}")
if descuento_extra > 0:
    print(f"El descuento aplicado fue de: {descuento} y un descuento extra de {descuento_extra}")
elif descuento > 0:
    print(f"El descuento aplicado fue de: {descuento}")
print(f"El total con descuento es de: {total_con_descuento_extra}")
