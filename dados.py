import random

def tipo_dado_valido(t):
    return t in (4, 6, 8, 10, 12, 20)

def lanzar_dados(n, t=6):
    if not tipo_dado_valido(t):
        raise ValueError("Tipo de dado incorrecto")
    return [random.randint(1, t) for _ in range(n)]

def relanzar_decision(decision, lista_dados, t):
    nueva_lista = []
    for i in range(len(lista_dados)):
        if i < len(decision) and decision[i] == 'r':
            nueva_lista.append(random.randint(1, t))
        else:
            nueva_lista.append(lista_dados[i])
    return nueva_lista

def encontrar(lista_datos, valor_umbral):
    return [i for i in range(len(lista_datos)) if lista_datos[i] <= valor_umbral]

def relanzar_indices(lista_indices, lista_dados, t):
    nueva_lista = lista_dados.copy()
    for i in lista_indices:
        nueva_lista[i] = random.randint(1, t)
    return nueva_lista

def puntuacion(lista_dados):
    return sum(lista_dados)