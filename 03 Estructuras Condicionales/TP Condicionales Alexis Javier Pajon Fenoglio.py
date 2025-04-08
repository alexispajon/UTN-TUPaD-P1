# Actividad 1
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Es mayor de edad.")

#Actividad 2
notaUsuario = int(input("Ingresa tu nota: "))
if notaUsuario >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")

#Actividad 3
numUsuario = int(input("Ingresa un número: "))
if numUsuario % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Porfavor ingrese un número par")

#Actividad 4
edadUsuario = int(input("Ingrese su edad: "))
if edadUsuario < 12:
    print("Usted esta en la categoría: Niño ")
elif 12 <= edadUsuario < 18:
    print("Usted esta en la categoría: Adolescente")
elif 18 <= edadUsuario < 30:
    print("Usted esta en la categoría: Adulto joven")
elif edadUsuario >= 30:
    print("Usted esta en la categoría: Adulto")
else:
    print("Ingrese una edad válida")

#Actividad 5
contraseña = input("Ingresa una contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Actividad 6
import random
import statistics
numerosAleatorios = [random.randint(1, 100) for i in range(50)]
media = statistics.mean(numerosAleatorios)
mediana = statistics.median(numerosAleatorios)
moda = statistics.mode(numerosAleatorios)
print(f"Números aleatorios: {numerosAleatorios}")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if moda < media < mediana:
    print("Sesgo negativo (asimetría hacia la izquierda).")
elif moda > media > mediana:
    print("Sesgo positivo (asimetría hacia la derecha).")
else:
    print("No hay sesgo claro.")

#Actividad 7
texto = input("Ingresa una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

#Actividad 8
nombre = input("Ingresa tu nombre: ")
print("\nElige una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.capitalize())
else:
    print("Opción no válida.")

#Actividad 9
magnitudTerremoto = int(input("Ingrese la magnitud del terremoto: "))
if magnitudTerremoto < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitudTerremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitudTerremoto < 5:
    print("Moderado (sentido por personas, pero no genera daños)")
elif 5 <= magnitudTerremoto < 6:
    print("Fuerte (puede causar daño en estructuras débiles)")
elif 6 <= magnitudTerremoto < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitudTerremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Ingrese una magnitud válida")

#Actividad 10
hemisferio = input("Ingrese el hemisferio donde se encuentra (N/S)").strip().upper()
mes = int(input("Ingrese el mes actuañ (1 al 12): "))
dia = int(input("Ingrese el día actual (1 al 31): "))
def estacionNorte(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano"
    else:
        return "Otoño"
def estacionSur(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"
if hemisferio == "N":
    estacion = estacionNorte(mes, dia)
elif hemisferio == "S":
    estacion = estacionSur(mes, dia)
else:
    estacion = "Hemisferio no válido"
print(f"Te encuentras en {estacion}.")

