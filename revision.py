# Usuarios vendedores de MercadoLibre
# Cargar 10 usuarios/vendedores de MercadoLibre con sus respectivas
# publicaciones.
# ● Los datos que se cargarán son:
# ● Nombre de usuario
# ● Edad (validar)
# ● Cantidad de productos (validar-número entero positivo).
# ● Número de publicaciones (validar-número entero positivo, hasta 1000).
# ● Tipo ("producto", "servicio", "subasta")
# ● Cuenta activa ("si", "no")

# Tema B:

# 1. Cantidad de usuarios con la cuenta inactiva cuyo producto sea del tipo
# “servicio”, cuya edad no supere los 55 años.

# 2. Nombre y tipo de publicacion de mayor edad con menos de 500
# publicaciones.

# 3. Porcentaje de cuentas activas.

# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron 
# del tipo “servicio”.

# 5. Determinar el tipo con menos publicaciones, cuya cuenta se encuentre
# “activa”.
contador_cuentas = 0
cont_ingresos = 0
contador_activas = 0
contador_productos_activo = 0
contador_subasta_activo = 0
contador_servicio_activo = 0
contador_servicio = 0
acumulador_edad = 0
contador_usuarios_servicio_menos_55 = 0
bandera_mayor_edad = 0
mayor_edad = 0

while cont_ingresos < 10:
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    while edad < 18:
        edad = int(input("REingrese su edad: "))
    cant_productos = int(input("ingrese la cantidad de productos: "))
    while cant_productos < 0:
        cant_productos = int(input("REingrese la cantidad de productos: "))
    num_publicaciones = int(input("ingrese un numero de publicaciones (no mayor a 1000): "))
    while num_publicaciones < 0 or num_publicaciones > 1000:
        num_publicaciones = int(input("ingrese un numero de publicaciones (no mayor a 1000): "))
    tipo = input("ingresa el tipo: ")
    while tipo != "producto" and tipo != "servicio" and tipo != "subasta":
        tipo = input("ingresa el tipo: ")
    cuenta_activa = input("ingrese cuanta activa (si/no): ")
    while cuenta_activa != "si" and cuenta_activa != "no":
        cuenta_activa = input("REIngrese cuanta activa (si/no): ")

# 1. Cantidad de usuarios con la cuenta inactiva cuyo producto sea del tipo
# “servicio”, cuya edad no supere los 55 años.

    contador_cuentas +=1

    if cuenta_activa:
        contador_activas +=1
    if tipo == "producto":
        contador_productos_activo =+1
    elif tipo =="subasta":
        contador_subasta_activo +=1
    else:
        contador_servicio_activo +=1
    if tipo == "servicio":
        contador_servicio +=1
        acumulador_edad += edad
    elif edad < 55:
        contador_usuarios_servicio_menos_55 =+1

    

# 2. Nombre y tipo de publicacion de mayor edad con menos de 500
# publicaciones.
    if num_publicaciones < 500:
        if bandera_mayor_edad == 0:
            mayor_edad = edad
            nombre_edad_mayor = nombre
            tipo_mayor_edad = tipo
            bandera_mayor_edad = 1
        elif edad > mayor_edad:
            mayor_edad = edad
            nombre_edad_mayor = nombre
            tipo_mayor_edad = tipo

# 3. Porcentaje de cuentas activas.

porcentaje_activas = (contador_activas / contador_cuentas) * 100
if contador_servicio > 0:
    promedio_edad = acumulador_edad / contador_servicio

# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron 
# del tipo “servicio”.

# 5. Determinar el tipo con menos publicaciones, cuya cuenta se encuentre
# “activa”.

if contador_productos_activo < contador_subasta_activo and contador_subasta_activo < contador_servicio_activo:
    menos_publicaciones = "subasta"
elif contador_servicio_activo < contador_subasta_activo and contador_subasta_activo < contador_productos_activo:
    menos_publicaciones = "servicio"
else:
    menos_publicaciones = "producto"

if contador_usuarios_servicio_menos_55 >0:
    print(f"1. Cantidad de usuarios con la cuenta inactiva cuyo producto sea del tipo “servicio”, cuya edad no supere los 55 años. {contador_usuarios_servicio_menos_55}")
else:
    print("NO se ingreso.")

if bandera_mayor_edad > 0:
    print(f"# 2. Nombre y tipo de publicacion de mayor edad con menos de 500 publicaciones.{nombre_edad_mayor} y {tipo_mayor_edad}")
else:
    print("no se ingreso lo pedido. ")

print(f"Porcentaje de cuentas activas: {porcentaje_activas} '%'")
if contador_servicio > 0:
    print(f"Promedio Edad de usuarios en pub. de tipo 'servicio': {promedio_edad}")
else: 
    print("No hay publicaciones de tipo 'servicio'") 



