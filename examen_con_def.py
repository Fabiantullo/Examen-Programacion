def obtener_datos_encuestado():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad (No menor a 18): "))
    while edad < 18:
        edad = int(input("REIngrese su edad (No menor a 18): "))
    empleado = input("Ingrese si esta empleado (si/no): ")
    while empleado not in ["si", "no"]:
        empleado = input("REIngrese si esta empleado (si/no): ")
    genero = input("Ingrese su genero (Masculino, Femenino, Otro): ")
    while genero not in ["Masculino", "Femenino", "Otro"]:
        genero = input("REIngrese su genero (Masculino, Femenino, Otro): ")
    voto = input("Ingrese su voto (APPLE, DUNKIN, IKEA): ")
    while voto not in ["APPLE", "DUNKIN", "IKEA"]:
        voto = input("REIngrese su voto (APPLE, DUNKIN, IKEA): ")
    return nombre, edad, empleado, genero, voto

def main():
    cantidad_encuestados_masculinos = 0
    nombre_menor_edad_apple = ""
    genero_menor_edad_apple = ""
    edad_menor_edad_apple = 0
    porcentaje_femenino_ikea = 0
    total_femenino = 0
    votos = {"APPLE": 0, "DUNKIN": 0, "IKEA": 0}
    edades_empleados = 0
    edades_no_empleados = 0
    contador_empleados = 0
    contador_no_empleados = 0

    seguir = "si"
    while seguir == "si":
        nombre, edad, empleado, genero, voto = obtener_datos_encuestado()
        if genero == "Masculino":
            if edad >= 18 and edad <= 25 or edad >= 36 and edad <= 49 or voto == "IKEA":
                cantidad_encuestados_masculinos += 1
        if voto == "APPLE":
            if edad < edad_menor_edad_apple or edad_menor_edad_apple == 0:
                nombre_menor_edad_apple = nombre
                genero_menor_edad_apple = genero
                edad_menor_edad_apple = edad
            votos["APPLE"] += 1
        elif voto == "DUNKIN":
            votos["DUNKIN"] += 1
        elif voto == "IKEA":
            votos["IKEA"] += 1
            if genero == "Femenino":
                porcentaje_femenino_ikea += 1
                total_femenino += 1
        if empleado == "si":
            contador_empleados += 1
            edades_empleados += edad
        else:
            contador_no_empleados += 1
            edades_no_empleados += edad
        seguir = input("Desea continuar (si/no): ")

    print("Resultados:")
    print("Cantidad de encuestados masculinos entre 18 y 25 o entre 36 y 49 o que votaron por IKEA:", cantidad_encuestados_masculinos)
    print("Nombre del menor edad que voto por APPLE:", nombre_menor_edad_apple)
    print("Genero del menor edad que voto por APPLE:", genero_menor_edad_apple)
    print("Edad del menor edad que voto por APPLE:", edad_menor_edad_apple)
    print("Porcentaje de mujeres que votaron por IKEA:", (porcentaje_femenino_ikea / total_femenino) * 100 if total_femenino > 0 else 0)
    print("Edad promedio de los empleados:", edades_empleados / contador_empleados if contador_empleados > 0 else 0)
    print("Edad promedio de los no empleados:", edades_no_empleados / contador_no_empleados if contador_no_empleados > 0 else 0)
    print("Empresa con mas votos:", max(votos, key=votos.get))

if __name__ == "__main__":
    main()