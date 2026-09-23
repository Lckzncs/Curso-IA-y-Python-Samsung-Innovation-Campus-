import random

CASILLAS = 5
FRUTAS = ["🍎", "🍋", "🍇"]

print("============================")
print("   🎰 MÁQUINA TRAGAPERRAS   ")
print("============================")
print(f"Casillas: {CASILLAS}  |  Frutas: {' '.join(FRUTAS)}")
print()

print(">>> TU TURNO <<<")
tiradas_humano = []

entrada = input("Pulsa ENTER para girar o escribe 'stop' para parar: ")
while entrada.lower() != "stop":
    casillas = [random.choice(FRUTAS) for _ in range(CASILLAS)]
    tiradas_humano.append(casillas)
    print(f"  Tirada {len(tiradas_humano)}: {' '.join(casillas)}")
    entrada = input("Pulsa ENTER para girar o escribe 'stop' para parar: ")

if tiradas_humano:
    ultima_humano = tiradas_humano[-1]
    puntos_humano = max(ultima_humano.count(f) for f in FRUTAS)
else:
    ultima_humano = []
    puntos_humano = 0

print(f"\nTu última tirada: {' '.join(ultima_humano) if ultima_humano else 'Sin tiradas'}")
print(f"Tu puntuación: {puntos_humano} puntos")

print("\n>>> TURNO DEL ORDENADOR <<<")
num_tiradas = random.randint(1, 6)
tiradas_pc = []

for i in range(num_tiradas):
    casillas = [random.choice(FRUTAS) for _ in range(CASILLAS)]
    tiradas_pc.append(casillas)
    print(f"  Tirada {i + 1}: {' '.join(casillas)}")

ultima_pc = tiradas_pc[-1]
puntos_pc = max(ultima_pc.count(f) for f in FRUTAS)

print(f"\nÚltima tirada del ordenador: {' '.join(ultima_pc)}")
print(f"Puntuación del ordenador: {puntos_pc} puntos")

print()
print("============================")
print("      RESULTADO FINAL       ")
print("============================")
print(f"  Tu puntuación:            {puntos_humano}")
print(f"  Puntuación del ordenador: {puntos_pc}")
print()

if puntos_humano > puntos_pc:
    print("🎉 ¡Ganaste!")
elif puntos_pc > puntos_humano:
    print("😞 Ganó el ordenador.")
else:
    print("🤝 ¡Empate!")
