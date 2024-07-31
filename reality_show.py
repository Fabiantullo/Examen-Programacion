"""
Enunciado:

De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos

Informar:

a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()
"""

contador = 0
acumulador_edades = 0
acumulador_votos = 0

while contador < 3:
    nombre_ingresado = input("Ingrese el nombre del jugador:  ")

    edad_ingresada = int(input("Ingrese la edad (Mayor a 25):  "))
    while edad_ingresada < 25:
        edad_ingresada = int(input("REIngrese la edad (Mayor a 25):  "))

    cantidad_votos_ingresada = int(input("Ingrese la cantidad de votos (No menor a 0):  "))
    while cantidad_votos_ingresada < 0:
        cantidad_votos_ingresada = int(input("REIngrese la cantidad de votos (No menor a 0):  "))

    if contador == 0:
        nombre_candidato_mas_votos = nombre_ingresado
        votos_candidato_mas_votos = cantidad_votos_ingresada

        nombre_candidato_menos_votos = nombre_ingresado
        edad_candidato_menos_votos = edad_ingresada
        votos_candidato_menos_votos = cantidad_votos_ingresada

    elif cantidad_votos_ingresada > votos_candidato_mas_votos:
        nombre_candidato_mas_votos = nombre_ingresado
        votos_candidato_mas_votos = cantidad_votos_ingresada

    elif cantidad_votos_ingresada < votos_candidato_menos_votos:
        nombre_candidato_menos_votos = nombre_ingresado
        edad_candidato_menos_votos = edad_ingresada
        votos_candidato_menos_votos = cantidad_votos_ingresada
    
    acumulador_edades += edad_ingresada
    acumulador_votos += cantidad_votos_ingresada
    contador += 1

# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
promedio_edades = acumulador_edades / contador

print(f"El candidato con mas votos es: {nombre_candidato_mas_votos}.")
print(f"El candidato con menos votos es: {nombre_candidato_menos_votos} y su edad es {edad_candidato_menos_votos}.")
print(f"El promedio de edades es:  {promedio_edades}.")
print(f"El total de votos es: {acumulador_votos}")

