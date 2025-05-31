import math

# Act. 1: Función "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Act 2: Función "saludo personalizado"
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Act 3: Función "información personal"
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Act 4: Funciones "área y perímetro"
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Act 5: Función "segundos a horas"
def segundos_a_horas(segundos):
    return segundos / 3600

# Act 6: Función "tabla de multiplicar"
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Act 7: Función "operaciones básicas"
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# Act 8: Función "calcular IMC"
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Act 9: Función "Celsius a Fahrenheit"
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Act 10: Función "promedio de 3 números"
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal
# 1
imprimir_hola_mundo()

# 2
nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))

# 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# 5
segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

# 6
numero_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# 7
a = float(input("Ingrese el primer número para operaciones básicas: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# 9
celsius = float(input("Ingrese una temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}")

# 10
n1 = float(input("Ingrese el primer número para promedio: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")
