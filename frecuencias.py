class Frecuencias:
    def __init__(self):
        self.__cadena = ""
        self.__frecuencias = {}

    def add_cadena(self, nueva_cadena):
        self.__cadena += nueva_cadena
        for caracter in nueva_cadena:
            if caracter.isalpha():
                letra = caracter.lower()
                if letra in self.__frecuencias:
                    self.__frecuencias[letra] += 1
                else:
                    self.__frecuencias[letra] = 1

    def add_fichero(self, nombre_fichero):
        with open(nombre_fichero, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        self.add_cadena(contenido)

    def get_cadena(self):
        return self.__cadena

    def print_fichero(self, nombre_fichero):
        with open(nombre_fichero, 'w', encoding='utf-8') as archivo:
            archivo.write(self.__cadena)

    def frecuencia_relativa(self, simbolo):
        total_letras = sum(self.__frecuencias.values())
        if total_letras == 0:
            return 0.0
        
        letra = simbolo.lower()
        apariciones = self.__frecuencias.get(letra, 0)
        return (apariciones / total_letras) * 100

    def __str__(self):
        lineas = []
        letras_ordenadas = sorted(self.__frecuencias.keys())
        for letra in letras_ordenadas:
            num_veces = self.__frecuencias[letra]
            lineas.append(f"La letra {letra} ha aparecido {num_veces} veces.")
        return "\n".join(lineas)