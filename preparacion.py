"De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos."
#Nombre
#Tipo (gato ,perro o exotico)
#Peso ( entre 10 y 80)
#Sexo( F o M )
#Edad(mayor a 0)
#Pedir datos por prompt y mostrar por print, se debe informar:
#Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
#Informe B- El porcentaje de mascotas femeninas y el de las masculinas.
#Informe C -El tipo de la mascota más pesada
#Informe D- El nombre del gato más joven
#Informe E- El promedio de peso de todas las mascotas
contador = 0
contador_gatos = 0
contador_perros = 0
contador_exoticos = 0
contador_femeninas = 0
contador_masculinas = 0
peso_mascota_pesada = 0
edad_gato_joven = 0
acumulador_peso = 0

while contador < 5:
    nombre_ingresado = input("Ingrese el nombre de la mascota: ")

    tipo_ingresado = input("Ingrese el tipo de la mascota (gato, perro o exotico):  ")
    while tipo_ingresado != "gato" and tipo_ingresado != "perro" and tipo_ingresado != "exotico":
        tipo_ingresado = input("ReIngrese el tipo de la mascota (gato, perro o exotico):  ")

    peso_ingresado = int(input("Ingrese el peso de su mascota (entre 10 y 80):  "))
    while peso_ingresado < 10 or peso_ingresado > 80:
        peso_ingresado = int(input("Reingrese el peso de su mascota (entre 10 y 80):  "))

    sexo_ingresado = input("Ingrese el sexo de la mascota (F o M):  ")
    while sexo_ingresado != "F" and sexo_ingresado != "M":
        sexo_ingresado = input("Reingrese el sexo de la mascota (F o M):  ")

    edad_ingresada = int(input("Ingrese la edad de la mascota (mayor a 0):  "))
    while edad_ingresada < 0:
        edad_ingresada = int(input("Reingrese la edad de la mascota (mayor a 0):  "))

    match tipo_ingresado:
        case "gato":
            if contador_gatos == 0:
                edad_gato_joven = edad_ingresada
                nombre_gato_joven = nombre_ingresado
            elif edad_ingresada < edad_gato_joven:
                edad_gato_joven = edad_ingresada
                nombre_gato_joven = nombre_ingresado
            contador_gatos += 1
        
        case "perro":
            contador_perros += 1
        case _ :
            contador_exoticos += 1
    
    match sexo_ingresado:
        case "F":
            contador_femeninas += 1
        case _ :
            contador_masculinas += 1

    if contador == 0:
        peso_mascota_pesada = peso_ingresado
        tipo_mascota_pesada = tipo_ingresado
    elif peso_ingresado > peso_mascota_pesada:
        peso_mascota_pesada = peso_ingresado
        tipo_mascota_pesada = tipo_ingresado

    acumulador_peso += peso_ingresado
    contador += 1

#Informe B- El porcentaje de mascotas femeninas y el de las masculinas.
porcentaje_femeninas = (contador_femeninas / contador) * 100
porcentaje_masculinas = (contador_masculinas / contador) * 100
#Informe E- El promedio de peso de todas las mascotas
promedio_peso = acumulador_peso / contador

#Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
if contador_gatos > contador_perros and contador_gatos > contador_exoticos:
    print("El tipo mas ingresado fue gato")
elif contador_perros > contador_exoticos:
    print("El tipo mas ingresado fue perro")
else:
    print("El tipo mas ingresado fue exotico")
#Informe B- El porcentaje de mascotas femeninas y el de las masculinas. 
print(f"El porcentaje de mascotas femeninas es {porcentaje_femeninas}%")
print(f"El porcentaje de mascotas masculinas es {porcentaje_masculinas}%")
#Informe C -El tipo de la mascota más pesada
print(f"El tipo de la mascota más pesada es {tipo_mascota_pesada}")
#Informe D- El nombre del gato más joven
print(f"El nombre del gato más joven es {nombre_gato_joven}")
#Informe E- El promedio de peso de todas las mascotas
print(f"El promedio de peso de todas las mascotas es {promedio_peso}")