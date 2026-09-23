import random

numeros = []
for i in range(100):
    numeros.append(random.randrange(1, 10002, 2))

primos = 0
for n in numeros:
    contador = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            contador += 1
    if n >= 2 and contador == 0:
        primos += 1

print("Números elegidos:", numeros)
print("Cantidad de primos:", primos)
