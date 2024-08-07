#Las posibles marcas son las siguientes: Samsung, Starbucks o Zara.

#Para ello, se llevará a cabo una encuesta a través de un sistema de votación digital, con el fin de conocer las preferencias de los participantes (sin un número específico de encuestados). Se recopilará la siguiente información de cada participante:

#Nombre
#Edad (no menor a 18 años)
#Está empleado (sí - no)
#Género (Masculino - Femenino - Otro)
#Voto (SAMSUNG, STARBUCKS, ZARA)
#Se necesita saber:

#Cantidad de encuestados desempleados que votaron por STARBUCKS o ZARA, cuya edad esté entre 25 y 50 años inclusive.
#Nombre y voto del encuestado de género Masculino con menor edad.
#Porcentaje de votos de cada género.
#Promedio de edad de los encuestados de género Femenino que votaron ZARA.
#Determinar cuál fue el género que tuvo más encuestados.

seguir = "si"
encuestados_desempleados_voto = 0
contador = 0

voto_masculino = 0
voto_femenino = 0
voto_otro = 0
edad_masculino_menor_edad = 0
acumulador_edad_femenino_zara = 0
contador_edad_femenino_zara = 0

while seguir == "si":
    nombre_ingresado = input("Ingrese su nombre: ")
    
    edad_ingresada = input("Ingrese su edad (mayor a 18): ")
    while edad_ingresada < 18:
        edad_ingresada = input("REIngrese su edad (mayor a 18): ")
        
    empleado_ingresado = input("¿Esta empleado? (si/no): ")
    while empleado_ingresado != "si" and empleado_ingresado != "no":
        empleado_ingresado = input("¿Reingrese, Esta empleado? (si/no): ")
        
    genero_ingresado = input("Ingrese su genero (Masculino, Femenino o Otro): ")
    while genero_ingresado != "Masculino" and genero_ingresado != "Femenino" and genero_ingresado != "Otro":
        genero_ingresado = input("REIngrese su genero (Masculino, Femenino o Otro): ")
    
    voto_ingresado = input("Ingrese su voto (SAMSUNG, STARBUCKS o ZARA): ")
    while voto_ingresado != "SAMSUNG" and voto_ingresado != "STARBUCKS" and voto_ingresado != "ZARA":
        voto_ingresado = input("REIngrese su voto (SAMSUNG, STARBUCKS o ZARA): ")
        
    #Cantidad de encuestados desempleados que votaron por STARBUCKS o ZARA, cuya edad esté entre 25 y 50 años inclusive.
    match voto_ingresado:
        case "STARBUCKS" | "ZARA":
            if edad_ingresada >= 25 and edad_ingresada <= 50:
                if empleado_ingresado == "no":
                    encuestados_desempleados_voto += 1
                    
    #Nombre y voto del encuestado de género Masculino con menor edad.
    match genero_ingresado:
        case "Masculino":
            if voto_masculino == 0:
                nombre_masculino_menor_edad = nombre_ingresado
                voto_masculino_menor_edad = voto_ingresado
                edad_masculino_menor_edad = edad_ingresada
            elif edad_ingresada < edad_masculino_menor_edad:
                nombre_masculino_menor_edad = nombre_ingresado
                voto_masculino_menor_edad = voto_ingresado
                edad_masculino_menor_edad = edad_ingresada
            voto_masculino += 1
        case "Femenino":
            voto_femenino += 1
            if voto_ingresado == "ZARA":
                acumulador_edad_femenino_zara += edad_ingresada
                contador_edad_femenino_zara += 1
                
        case _:
            voto_otro += 1
        
    contador += 1
    seguir = input("¿Desea seguir? (si/no): ")
        
porcentaje_masculino = (voto_masculino / contador) * 100
porcentaje_femenino = (voto_femenino / contador) * 100
porcentaje_otro = (voto_otro / contador) * 100

promedio_edad = acumulador_edad_femenino_zara / contador_edad_femenino_zara

#Cantidad de encuestados desempleados que votaron por STARBUCKS o ZARA, cuya edad esté entre 25 y 50 años inclusive.
#Nombre y voto del encuestado de género Masculino con menor edad.
#Porcentaje de votos de cada género.
#Promedio de edad de los encuestados de género Femenino que votaron ZARA.
#Determinar cuál fue el género que tuvo más encuestados.

print(f"La cantidad de encuestados desempleados que votaron por STARBUCKS o ZARA cuya edad esta entre 25 y 50 es: {encuestados_desempleados_voto}")
print(f"El nombre y voto del encuestado de género Masculino con menor edad {nombre_masculino_menor_edad} y su edad es {edad_masculino_menor_edad}")
print(f"El porcentaje de votos de cada género es: Masculino: {porcentaje_masculino:.2f}% Femenino: {porcentaje_femenino:.2f}% Otro: {porcentaje_otro:.2f}%")
print(f"El promedio de edad de los encuestados de género Femenino que votaron ZARA es: {promedio_edad}")
if voto_masculino > voto_femenino and voto_masculino > voto_otro:
    print("El género que tuvo más encuestados es Masculino")
elif voto_femenino and voto_otro:
    print("El género que tuvo más encuestados es Femenino")
else:
    print("El género que tuvo más encuestados es Otro")