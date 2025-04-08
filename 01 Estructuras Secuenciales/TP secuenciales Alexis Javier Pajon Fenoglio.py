# Actividad 1
print("Hola mundo")

# Actividad 2
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Actividad 4
pi = 3.14
radio = float(input("Ingresa el radio del círculo: "))
area = pi * (radio ** 2) 
perimetro = 2 * pi * radio  
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Actividad 5
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600  
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Actividad 6
numero = int(input("Ingresa un número: "))
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Actividad 7
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
if num1 == 0 or num2 == 0:
    print("Error: Los números deben ser distintos de 0.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"\nResultados:")
    print(f"{num1} + {num2} = {suma}")
    print(f"{num1} - {num2} = {resta}")
    print(f"{num1} * {num2} = {multiplicacion}")
    print(f"{num1} / {num2} = {division:.2f}")

# Actividad 8
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"\nTu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Actividad 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"\n{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

# Actividad 10
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"\nEl promedio de los tres números es: {promedio:.2f}")
