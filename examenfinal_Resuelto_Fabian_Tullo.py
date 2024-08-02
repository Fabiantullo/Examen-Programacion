# Programación Inicial Examen Final Tema C TM
# Fabian Andres Tullo Div.105 DNI: 45419371

# UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
# franquicia que se insertará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
# propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
# Se ingresa de cada encuestado:
# ● nombre
# ● edad (no menor a 18)
# ● está empleado (si-no)
# ● género (Masculino - Femenino - Otro)
# ● voto (APPLE, DUNKIN, IKEA)
# Se necesita saber:
# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
# 25 o entre 36 y 49 o que votaron por IKEA.
# 2. Nombre y género del encuestado de menor edad que votó por APPLE.
# 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
# edad mayor a 25 años.
# 4. Edad promedio de los encuestados que están o no empleados (de cada
# uno).
# 5. Determinar cuál fue la franquicia más votada

seguir = "si"
encuestados_masculinos = "¡No hay!"
edad_menor_edad_apple = 0
voto_ikea_femenino_mayor_25 = 0
votos_apple = 0
votos_ikea = 0
votos_dunkin = 0
acumulador_edad_empleados = 0
contador_empleados = 0
acumulador_edad_no_empleados = 0
contador_no_empleados = 0
contador = 0
edad_promedio_empleados = "¡No hay empleados!"
edad_promedio_no_empleados = "¡No hay no-empleados!"

while seguir == "si":
    nombre_ingresado = input("Ingrese su nombre:  ")
    try:
        edad_ingresada = int(input("Ingrese su edad (No menor a 18):  "))
        while edad_ingresada < 18:
            edad_ingresada = int(input("REIngrese su edad (No menor a 18):  "))
    except ValueError:
        print("Solo se permiten numeros")
        continue 
    empleado_ingreso = input("Ingrese si esta empleado (si/no):  ")
    while empleado_ingreso != "si" and empleado_ingreso != "no":
        empleado_ingreso = input("REIngrese si esta empleado (si/no):  ")

    genero_ingresado = input("Ingrese su genero (Masculino, Femenino, Otro):  ")
    while genero_ingresado != "Masculino" and genero_ingresado != "Femenino" and genero_ingresado != "Otro":
        genero_ingresado = input("REIngrese su genero (Masculino, Femenino, Otro):  ")

    voto_ingresado = input("Ingrese su voto (APPLE, DUNKIN, IKEA):  ")
    while voto_ingresado != "APPLE" and voto_ingresado != "DUNKIN" and voto_ingresado != "IKEA":
        voto_ingresado = input("REIngrese su voto (APPLE, DUNKIN, IKEA):  ")

    # 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
    # 25 o entre 36 y 49 o que votaron por IKEA.
    # 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
    # edad mayor a 25 años.
    match genero_ingresado:
        case "Masculino":
            if edad_ingresada > 18 and edad_ingresada < 25:
                encuestados_masculinos += 1

            elif edad_ingresada > 36 and edad_ingresada < 49:
                encuestados_masculinos += 1
            
            elif voto_ingresado == "IKEA":
                encuestados_masculinos += 1

        case "Femenino":
            if voto_ingresado == "IKEA":
                if edad_ingresada > 25:
                    voto_ikea_femenino_mayor_25 += 1

    # 2. Nombre y género del encuestado de menor edad que votó por APPLE.
    # 5. Determinar cuál fue la franquicia más votada

    match voto_ingresado:
        case "APPLE":
            if votos_apple == 0:
                nombre_menor_edad_apple = nombre_ingresado
                genero_menor_edad_apple = genero_ingresado
                edad_menor_edad_apple = edad_ingresada
                bandera_menor_edad_apple = 1
            elif edad_ingresada < edad_menor_edad_apple:
                nombre_menor_edad_apple = nombre_ingresado
                genero_menor_edad_apple = genero_ingresado
                edad_menor_edad_apple = edad_ingresada
            votos_apple += 1

        case "DUNKIN":
            votos_dunkin += 1

        case _:
            votos_ikea += 1

    # 4. Edad promedio de los encuestados que están o no empleados (de cada
    match empleado_ingreso:
        case "si":
            acumulador_edad_empleados += edad_ingresada
            contador_empleados += 1
        
        case _:
            acumulador_edad_no_empleados += edad_ingresada
            contador_no_empleados += 1

    contador += 1
    seguir = input("¿Quiere seguir? (si/no):  ")

porcentaje_femenino_ikea = (voto_ikea_femenino_mayor_25 / contador) * 100
try:
    edad_promedio_empleados = acumulador_edad_empleados / contador_empleados
except ZeroDivisionError:
    print("No se encontro empleados registrados.")
    
try:
    edad_promedio_no_empleados = acumulador_edad_no_empleados / contador_no_empleados
except ZeroDivisionError:
    print("No se encontro no-empleados registrados.")

print(f"La cantidad de encuestados Masculinos, cuya edad esta entre 18 y 25 o entre 36 y 49 o que votaron por IKEA fue de: {encuestados_masculinos}.")
print(f"El encuestado con menor edad que voto por APPLE fue: {nombre_menor_edad_apple} y su genero es {genero_menor_edad_apple}.")
print(f"El porcentaje de genero Femenino que voto por IKEA y su edad es mayor a 25 es:  {porcentaje_femenino_ikea:.2f}%")
print(f"La edad promedio de los encuestados que estan empleados fue de: {edad_promedio_empleados} y la de no empleados fue de {edad_promedio_no_empleados}")
if votos_apple > votos_dunkin and votos_apple > votos_ikea:
    print(f"La empresa mas votada fue APPLE.")
elif votos_dunkin > votos_ikea:
    print(f"La empresa mas votada fue DUNKIN.")
else:
    print(f"La empresa mas votada fue IKEA.")