# Damian Sosa
# Examen Final

# UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva franquicia que se insertará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
# Se ingresa de cada encuestado:
# ● nombre
# ● edad (no menor a 18)
# ● está empleado (si-no)
# ● género (Masculino - Femenino - Otro)
# ● voto (APPLE, DUNKIN, IKEA)
# Se necesita saber:
# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.
# 2. Nombre y género del encuestado de menor edad que votó por APPLE.
# 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.
# 4. Edad promedio de los encuestados que están o no empleados (de cada uno).
# 5. Determinar cuál fue la franquicia más votada.

seguir = "Si"
encuestados_genero_masculino = 0
primer_voto_apple = 0
encuestados_género_femenino_votaron_ikea_edad_mayor_25 = 0
acumulador_edad_empleados = 0
acumulador_edad_desempleados = 0
total_encuestados_empleados = 0
total_encuestados_desempleados = 0
total_votos_apple = 0
total_votos_dunkin = 0
total_votos_ikea = 0
total_votantes = 0

while seguir == "Si":
    
    nombre_del_encuestado = input("Ingrese su nombre: ")
    
    edad_del_encuestado = int(input("Ingrese su edad (Mayor a 18): "))
    while edad_del_encuestado < 18:
        edad_del_encuestado = int(input("Reingrese su edad: "))

    situacion_laboral = input("Ingrese su situacion laboral (Empleado - Desempleado): ")
    while situacion_laboral != "Empleado" and situacion_laboral != "Desempleado":
        situacion_laboral = input("Reingrese su sitaucion laboral: ")
    
    genero_del_encuestado = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    while genero_del_encuestado != "Masculino" and genero_del_encuestado != "Femenino" and genero_del_encuestado != "Otro":
        genero_del_encuestado = input("Reingrese su genero: ")
    
    voto_ingresado = input("Ingrese su voto (APPLE, DUNKIN, IKEA): ")
    while voto_ingresado != "APPLE" and voto_ingresado != "DUNKIN" and voto_ingresado != "IKEA":
        voto_ingresado = input("Reingrese su voto: ")

# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.

    if genero_del_encuestado == "Masculino":
        if edad_del_encuestado > 18 and edad_del_encuestado < 25 or edad_del_encuestado > 36 and edad_del_encuestado < 49 or voto_ingresado == "IKEA":
            encuestados_genero_masculino += 1

# 2. Nombre y género del encuestado de menor edad que votó por APPLE.

    if voto_ingresado == "APPLE":
        if primer_voto_apple == 0:
            encuestado_de_menor_edad_voto_apple = edad_del_encuestado
            nombre_votante_apple = nombre_del_encuestado
            genero_votante_apple = genero_del_encuestado
            primer_voto_apple = 1
        elif edad_del_encuestado < encuestado_de_menor_edad_voto_apple:
            nombre_votante_apple = nombre_del_encuestado
            genero_votante_apple = genero_del_encuestado

# 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.

    if genero_del_encuestado == "Femenino":
        if voto_ingresado == "IKEA":
            if edad_del_encuestado > 25:
                encuestados_género_femenino_votaron_ikea_edad_mayor_25 += 1

# 4. Edad promedio de los encuestados que están o no empleados (de cada uno).

    if situacion_laboral == "Empleado":
        acumulador_edad_empleados += edad_del_encuestado
        total_encuestados_empleados += 1
    else:
        acumulador_edad_desempleados += edad_del_encuestado
        total_encuestados_desempleados += 1

# 5. Determinar cuál fue la franquicia más votada.

    if voto_ingresado == "APPLE":
        total_votos_apple += 1
    elif voto_ingresado == "DUNKIN":
        total_votos_dunkin += 1
    else:
        total_votos_ikea += 1

    total_votantes += 1

    seguir = input ("Desea continuar el programa Si o No: ")

porcentaje_genero_femenino_votaron_ikea_mayor_25 = encuestados_género_femenino_votaron_ikea_edad_mayor_25 * 100 / total_votantes

edad_promedio_encuestados_empleados = acumulador_edad_empleados / total_encuestados_empleados
edad_promedio_encuestados_desempleados = acumulador_edad_desempleados / total_encuestados_desempleados

print(f"La cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA son {encuestados_genero_masculino}.")
print(f"El encuestado de menor edad que votó por APPLE se llama {nombre_votante_apple} y su genero es {genero_votante_apple}.")
print(f"El porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años es {porcentaje_genero_femenino_votaron_ikea_mayor_25}.")
print(f"La edad promedio de los encuestados que estan empleados es {edad_promedio_encuestados_empleados}, y la de los encuestados desempleados es {edad_promedio_encuestados_desempleados}.")

if total_votos_apple > total_votos_dunkin and total_votos_apple > total_votos_ikea:
    print(f"La franquicia mas votada es Apple con {total_votos_apple} votos.")
elif total_votos_dunkin > total_votos_ikea:
    print(f"La franquicia mas votada es Dunkin con {total_votos_dunkin} votos.")
else:
    print(f"La franquicia mas votada es Ikea con {total_votos_ikea} votos.")