class Queue:
    def __init__(self):
        self.__elems = []

    def is_empty(self):
        return len(self.__elems) == 0

    def size(self):
        return len(self.__elems)

    def enqueue(self, elem):
        self.__elems.append(elem)
    
    def __init__(self):
        self.__elems = []

    def is_empty(self):
        return len(self.__elems) == 0

    def size(self):
        return len(self.__elems)

    def enqueue(self, elem):
        self.__elems.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("No puedes hacer dequeue sobre una cola vacía")
        return self.__elems.pop(0)

    def first(self):
        if self.is_empty():
            raise ValueError("La cola está vacía")
        return self.__elems[0]

    def __str__(self):
        return str(self.__elems)

    def __eq__(self, otra):
        if isinstance(otra, Queue):
            return self.__elems == otra._Queue__elems
        return False

    def __iter__(self):
        return _IteradorQueue(self.__elems)


class _IteradorQueue:
    def __init__(self, elems):
        self.elems = elems
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.elems):
            resultado = self.elems[self.indice]
            self.indice += 1
            return resultado
        raise StopIterationend(elem)

    def queue(self):
        return self.__elems.pop(0)

    def first(self):
        return self.__elems[0]

    def __str__(self):
        return str(self.__elems)

    def __eq__(self, otra):
        if isinstance(otra, Queue):
            return self.__elems == otra._Queue__elems
        return False

    def __iter__(self):
        return _IteradorQueue(self.__elems)


class _IteradorQueue:
    def __init__(self, elems):
        self.elems = elems
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.elems):
            resultado = self.elems[self.indice]
            self.indice += 1
            return resultado
        raise StopIteration