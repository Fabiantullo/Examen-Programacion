"""

Se realiza un estudio de mercado para determinar cuál será la nueva franquicia 
que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes:
    The north face
    Zara
    Bershka

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, 
con el propósito de conocer cuáles son los gustos de los encuestados.

Datos a ingresar:
    Nombre del encuestado
    Edad (no menor a 18)
    Género (Masculino - Femenino - Otro)
    Voto (STARBUCKS, MCDONALDS, ZARA, KFC)
    Situación Laboral (Empleado - Desempleado)



Consignas:
    a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
    b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
    c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
    d-Quien de todos los sexos fue el que mas votó por Zara.
    """

seguir = "si"
bandera_zara = 0
edad_mayor_zara = 0
edad_otro_genero = 0
desempleado_starbucks = 0
contador_zara_masculino = 0
contador_zara_femenino = 0
contador_zara_otro = 0

while seguir == "si":
    nombre_ingresado = input("Ingrese su nombre: ")

    edad_ingresada = int(input("Ingrese su edad: "))
    while edad_ingresada < 18:
        edad_ingresada = int(input("Reingrese su edad: "))

    genero_ingresado = input("Ingrese su genero (Masculino, Femenino o Otro):  ")
    while genero_ingresado != "Masculino" and genero_ingresado != "Femenino" and genero_ingresado != "Otro":
        genero_ingresado = input("Reingrese su genero:  ")

    voto_ingresado = input("Ingrese su voto (STARBUCKS, MCDONALDS, ZARA, KFC):  ")
    while voto_ingresado != "STARBUCKS" and voto_ingresado != "MCDONALDS" and voto_ingresado != "ZARA" and voto_ingresado != "KFC":
        voto_ingresado = input("Reingrese su voto:  ")
    situacion_laboral_ingresada = input("Ingrese su situacion laboral (Empleado o Desempleado):  ")
    while situacion_laboral_ingresada != "Empleado" and situacion_laboral_ingresada != "Desempleado":
        situacion_laboral_ingresada = input("Reingrese su situacion laboral:  ")

    match voto_ingresado:
        case "ZARA":
            if bandera_zara == 0:
                nombre_mayor_edad_zara = nombre_ingresado
                edad_mayor_zara = edad_ingresada    
                situacion_laboral_mayor_zara = situacion_laboral_ingresada
                bandera_zara = 1
            elif edad_mayor_zara < edad_ingresada:
                nombre_mayor_edad_zara = nombre_ingresado
                edad_mayor_zara = edad_ingresada    
                situacion_laboral_mayor_zara = situacion_laboral_ingresada
            match genero_ingresado:
                case "Masculino":
                    contador_zara_masculino += 1
                case "Femenino":
                    contador_zara_femenino += 1
                case _ :
                    contador_zara_otro += 1

        case "STARBUCKS":
            if edad_ingresada >= 30 and edad_ingresada <= 45:
                desempleado_starbucks += 1

    match genero_ingresado:
        case "Otro":
            if edad_ingresada > 60 and edad_ingresada < 70:
                nombre_otro_genero = nombre_ingresado
                voto_otro_genero = voto_ingresado
                edad_otro_genero = edad_ingresada
    seguir = input("¿Desea seguir? si/no")

    # a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
    # b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
    # c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
    # d-Quien de todos los sexos fue el que mas votó por Zara.

print(f"a-Nombre y situación laboral de la persona con mayor edad que voto por zara: {nombre_mayor_edad_zara} y {situacion_laboral_mayor_zara}.")
print(f"b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años: {nombre_otro_genero} y su voto fue {voto_otro_genero}")
print(f"c-Cantidad de encuestados desempleados que votaron por starbucks, cuya edad esta entre 30 y 45 años inclusive es: {desempleado_starbucks}")
if contador_zara_masculino > contador_zara_femenino and contador_zara_masculino > contador_zara_otro:
    print(f"d-El sexo que mas votó por zara es el masculino")
elif contador_zara_femenino > contador_zara_otro:
    print(f"d-El sexo que mas votó por zara es el femenino")
else:
    print(f"d-El sexo que mas votó por zara es el otro")