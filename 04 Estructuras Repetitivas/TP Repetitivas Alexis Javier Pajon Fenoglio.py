import random

#Actividad 1
for i in range(101):
    print(i)

#Actividad 2
num_usuario = input("Ingrese un número entero: ")
if num_usuario.startswith("-"):
    num_usuario = num_usuario[1:]              # En caso de ser negativo le quitamos el signo
cant_digitos = len(num_usuario)
print("El número tiene", cant_digitos, "dígitos.")

#Actividad 3
inicio = int(input("Ingrese el primer número entero:"))
final = int(input("Ingrese el segundo número entero:"))
mayor = max(inicio , final)                           #Nos aseguramos de que la variable inicio sea la menor y final la mayor
menor = min(inicio , final)
suma = 0
for numero in range (menor + 1, mayor):
    suma += numero 
print("La suma de los números entre los valores", inicio, "y", final, "es: ", suma)

#Actividad 4
suma_total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break                                    # Sale del bucle si el número es 0
    suma_total += numero  
print("La suma total es:", suma_total)

#Actividad 5
num_secreto = random.randint (0,9)
intentos = 0
while True:
    num_usuario = int(input("ingrese un número entre el 0 y el 9:"))
    intentos += 1
    if num_usuario == num_secreto:
        print("Enhorabuena, acertaste en" , intentos , "intentos")
        break
    else:
        print("Intenta de nuevo:")

#Actividad 6
for numero_act in range(100,-1, -1):
    if numero_act % 2 == 0:
        print (numero_act)

#Actividad 7
limite = int(input("Ingrese un número entero positivo: "))
if limite < 0:
    print("Por favor, ingrese un número positivo.") # Verificamos que sea positivo
else:
    suma = 0
    for numero in range(limite + 1):  # Va desde 0 hasta el número ingresado (incluido)
        suma += numero

    print("La suma de los números desde 0 hasta", limite, "es:", suma)

#Actividad 8
cantidad = 100
pares = 0          # Contadores
impares = 0
positivos = 0
negativos = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:    # Contar pares e impares
        pares += 1
    else:
        impares += 1

    if numero > 0:        # Contar positivos y negativos
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\nResultados:")
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)

#Actividad 9
cantidad = 100
suma_total = 0         
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_total += numero 
media = suma / cantidad
print("La media de los" , cantidad , "números ingresados es: ", media)

#Actividad 10
num_invertido = "."
num_sin_signo = "."
while True:
    num_usuario = input("Ingrese un número de 2 cifras o más: ")
    es_negativo = num_usuario.startswith("-")   # Guardamos si el número tiene signo negativo
    if es_negativo:                        
        num_sin_signo = num_usuario[1:]    # Eliminamos el signo para verificar longitud
    else: 
        num_sin_signo = num_usuario   
    if len(num_sin_signo) >= 2 and num_sin_signo.isdigit():   # Verificamos si tiene al menos 2 cifras
        break
    else:
        print("Número no válido. Debe tener al menos 2 cifras.")
num_invertido = num_sin_signo[::-1]
if es_negativo:
    num_invertido = "-" + num_invertido          # Si era negativo, le volvemos a poner el signo

print("El número invertido es:", num_invertido)