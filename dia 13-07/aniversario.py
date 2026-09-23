from datetime import date, timedelta

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

dia_especial = date(2025, 1, 13)
aniversario = dia_especial + timedelta(days=100)

print(f"Día especial: {dia_especial.day} de {meses[dia_especial.month - 1]} de {dia_especial.year}")
print(f"Aniversario de 100 días: {aniversario.day} de {meses[aniversario.month - 1]} de {aniversario.year}")
