# Act 1: Factorial de un número
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# Act 2: Serie de Fibonacci
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"fibonacci({i}) = {fibonacci(i)}")

# Act 3: Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Act 4: Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    if n == 0:
        return "0"
    else:
        return decimal_a_binario(n)

# Act 5: Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Act 6: Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Act 7: Contar bloques de pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Act 8: Contar dígitos
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


# PRUEBAS

if __name__ == "__main__":

# 1
    print("1) Factoriales hasta 5:")
    mostrar_factoriales(5)

#2
    print("\n2) Serie de Fibonacci hasta la posición 7:")
    mostrar_fibonacci(7)

#3
    print("\n3) Potencia 2^5:")
    print(potencia(2, 5))

#4
    print("\n4) Binario de 10:")
    print(convertir_a_binario(10))

#5
    print("\n5) Palabra 'reconocer' es palíndromo?")
    print(es_palindromo("reconocer"))

#6
    print("\n6) Suma de dígitos de 1234:")
    print(suma_digitos(1234))

#7
    print("\n7) Total de bloques para pirámide de base 4:")
    print(contar_bloques(4))

#8
    print("\n8) Contar dígito 2 en 12233421:")
    print(contar_digito(12233421, 2))
