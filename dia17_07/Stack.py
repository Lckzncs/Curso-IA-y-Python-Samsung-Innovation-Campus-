class Stack:

    def __init__(self):
        self.__elems = []

    def push(self, x):
        self.__elems.append(x)

    def pop(self):
        if self.is_empty():
            raise ValueError("Pop sobre pila vacía")
        return self.__elems.pop()

    def top(self):
        if self.is_empty():
            raise ValueError("Top sobre pila vacía")
        return self.__elems[-1]

    def extend(self, elementos):
        for elem in elementos:
            self.push(elem)

    def is_empty(self):
        return len(self.__elems) == 0

    def size(self):
        return len(self.__elems)

    def __str__(self):
        return f"Stack({self.__elems})"

    def __len__(self):
        return self.size()

    def __del__(self):
        print(f"La pila {id(self)} se ha destruido")

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
            
        if len(self) != len(other):
            return False
            
        iguales = True 
        x = 0
        
        while x < len(self) and iguales:
            if self._Stack__elems[x] != other._Stack__elems[x]:
                iguales = False
            x += 1
            
        return iguales

    def __iter__(self):
        return _IteradorStack(self.__elems)


class _IteradorStack:
    def __init__(self, datos):
        self.__datos = datos
        self.__indice = len(self.__datos) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice < 0:
            raise StopIteration

        resultado = self.__datos[self.__indice]
        self.__indice -= 1
        return resultado