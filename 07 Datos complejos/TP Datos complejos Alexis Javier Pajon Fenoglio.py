# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actividad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Actividad 3
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# Actividad 4
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese un nombre para buscar su número: ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# Actividad 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print("Frecuencia de palabras:", frecuencia)

# Actividad 6
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")

# Actividad 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 6, 7}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# Actividad 8
stock = {'Arroz': 20, 'Fideos': 15, 'Aceite': 10}
producto = input("Ingrese el nombre de un producto: ")
if producto in stock:
    agregar = int(input(f"Ingrese unidades a agregar a {producto}: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese el stock inicial: "))
    stock[producto] = nuevo_stock
print("Stock actualizado:", stock)

# Actividad 9
agenda_eventos = {('Lunes', '9:00'): 'Reunión',('Martes', '14:00'): 'Clase de programación',('Viernes', '11:00'): 'Consulta médica'}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
evento = agenda_eventos.get((dia, hora), "No hay eventos agendados.")
print(f"Evento en {dia} a las {hora}: {evento}")

# Actividad 10
paises = {'Argentina':'Buenos Aires','Francia':'París','España':'Madrid','Italia':'Roma'}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
