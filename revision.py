#Facundo Tomás Hernández 
#Comision 105
#Profesor Giovanni Luchetta

#Dr. Gregory Cat (Diagnostico Veterinario)

#Para el hospital Universitario Princeton-Plainsboro de Nueva Jersey.

#Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden atender 15 mascotas), para esto hay que considerar  los  siguientes  datos  y encasillarlos  en  ciertos  diagnósticos  para  poder  derivarlos  adecuadamente:

#●	Edad (Validar entre 1 y 20 años)
#●	Tipo: (Validar “gato”, “perro”, “hámster”)
#●	Peso: (Más de 0 kg)
#●	Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
#●	Vacuna antirrábica (validar “si”, ”no”)

#Tema A

#1.	Cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10 años, que se presentaron por problemas digestivos o parásitos.
#2.	El tipo de mascota más ingresada con problemas digestivos.
#3.	Edad y tipo de la mascota más vieja sin vacuna antirrábica.
#4.	Porcentaje de mascotas vacunadas y no vacunadas.
#5.	Promedio de edad de los perros.

contador_mascota = 0

edad_mascota = 0

cantidad_vacuna_digestivo_parasitos = 0

gato_problemas_digestivos = 0
perro_problemas_digestivos = 0
hamster_problemas_digestivos = 0

edad_mascota_sin_vacuna = 0
tipo_mascota_sin_vacuna = ""
bandera_mascota_sin_vacuna = 0

mascotas_vacunadas =0
mascotas_no_vacunadas = 0
total_vacunas = 0

suma_edades_perro = 0
contador_edades_perro = 0


while contador_mascota < 15:
    edad = int(input ("Ingrese la edad de la mascota: "))
    while edad < 1 or edad > 20:
        edad = int(input ("REIngrese la edad de la mascota (entre 1 y 20 años): "))
        
    tipo = input ("Ingrese el tipo de mascota: ")
    while tipo != "gato" and tipo != "perro" and tipo != "hámster":
        tipo = input ("REIngrese el tipo de mascota (gato,perro,hámster): ")
        
    peso = float (input("Ingrese el peso de la mascota solamente con números: "))
    while peso < 0:
        peso = float (input("REIngrese el peso de la mascota (superior a 0): "))

    diagnostico = input ("Ingrese el diagnóstico de la mascota: ")
    while diagnostico != "problemas digestivos" and diagnostico != "parásitos" and diagnostico != "infección":
        diagnostico = input ("REIngrese el diagnóstico (problemas digestivos, parásitos, infección): ")
        
    vacuna = input ("¿Tiene puesta la vacuna antirrábica? (si/no): ")
    while vacuna != "si" and vacuna != "no":
        vacuna = input ("Contestas solamente por si o por no: ")
        
    match vacuna:
        case "si":
            total_vacunas += 1
            mascotas_vacunadas += 1
            if edad > 5 and edad < 10:
                if diagnostico == "problemas digestivos" or diagnostico == "parásitos":
                    cantidad_vacuna_digestivo_parasitos += 1
        case "no":
            total_vacunas += 1
            mascotas_no_vacunadas += 1
            if bandera_mascota_sin_vacuna == 0:
                edad_mascota_sin_vacuna = edad
                tipo_mascota_sin_vacuna = tipo
                bandera_mascota_sin_vacuna = 1
            elif edad > edad_mascota_sin_vacuna:
                edad_mascota_sin_vacuna = edad
                tipo_mascota_sin_vacuna = tipo

    match tipo:
        case "gato":
            if diagnostico == "problemas digestivos":
                gato_problemas_digestivos += 1
        case "perro":
            suma_edades_perro += edad
            contador_edades_perro += 1
            if diagnostico == "problemas digestivos":
                perro_problemas_digestivos += 1
        case _:
                hamster_problemas_digestivos += 1
    contador_mascota += 1

porcentaje_vacunados = (mascotas_vacunadas/total_vacunas)*100
porcentaje_no_vacunados = (mascotas_no_vacunadas/total_vacunas)*100

if contador_edades_perro > 0:
    promedio_edad_perro = suma_edades_perro/contador_edades_perro
else:
    promedio_edad_perro = 0

mas_problemas_digestivos = ""
if gato_problemas_digestivos > perro_problemas_digestivos and gato_problemas_digestivos > hamster_problemas_digestivos:
    mas_problemas_digestivos = "gato"
elif perro_problemas_digestivos > hamster_problemas_digestivos and perro_problemas_digestivos > gato_problemas_digestivos:
    mas_problemas_digestivos = "perro"
elif hamster_problemas_digestivos > gato_problemas_digestivos and hamster_problemas_digestivos > perro_problemas_digestivos:
    mas_problemas_digestivos = "hámster"
else:
    mas_problemas_digestivos = "No hay una mascota con más problemas digestivos."

print(f"La cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10 años, que se presentaron por problemas digestivos o parásitos es de {cantidad_vacuna_digestivo_parasitos}")
print(f"El tipo de mascota más ingresada con problemas digestivos es {mas_problemas_digestivos}")
print(f"La edad de la mascota más vieja sin vacuna es {edad_mascota_sin_vacuna} y el es un {tipo_mascota_sin_vacuna}")
print(f"El porcentaje de vacunados es {porcentaje_vacunados:.2f}% y el de no vacunados es del {porcentaje_no_vacunados:.2f}%")
print(f"El promedio de edad de los perros es de {promedio_edad_perro}")
