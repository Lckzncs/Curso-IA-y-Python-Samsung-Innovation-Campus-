import random

numeros = []

for i in range(23):
    a = random.randint(2, 4)
    numeros.append(a)

print(numeros)
print("Suma:", sum(numeros))