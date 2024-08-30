import numpy as np
class listaSecuencial:
    __tamaño:int
    __ultimo:int
    __cantidad:int
    __arreglo:np.ndarray

    def __init__(self, xtam):
        self.__tamaño=xtam
        self.__ultimo=0
        self.__cantidad=0
        self.__arreglo=np.empty(self.__tamaño)

    def insertar(self, nuevo):
        if not self.lleno():
            if self.vacia():
                self.__arreglo[0] = nuevo
            else:
                i=0
                while nuevo > self.__arreglo[i] and i <= self.__ultimo:
                    i += 1                      #cuando sale, el [i] donde vas a meter al nuevo
                for j in range(self.__ultimo+1, i-1, -1):
                    self.__arreglo[j] = self.__arreglo[j-1]
                self.__arreglo[i]=nuevo
                self.__ultimo += 1
                self.__cantidad += 1
        else:
            print("La lista está llena")
    
    def busqueda(self, elemento):
        inicial=0
        final = self.__ultimo
        while inicial <= self.__ultimo:
            medio=(inicial + final) // 2
            valor_medio = self.__arreglo[medio]
            if valor_medio == elemento:
                posicion=medio
            elif valor_medio < self.__arreglo[medio]:
                inicial = medio + 1
            else:
                final = medio - 1
        return posicion

    def suprimir(self, pos):
        try:
            if pos < 0 or pos > self.__ultimo + 1:
                raise IndexError
            assert self.vacia()
            for i in range(pos, self.__ultimo+1):
                self.__arreglo[i]=self.__arreglo[i+1]
            print("El elemento fue eliminado")
        except IndexError:
            print("Posicion no válida")
        except AssertionError:
            print("La lista está vacía")


    def recuperar(self, pos):
        try:
            if pos < 0 or pos > self.__ultimo + 1:
                raise IndexError
            assert self.vacia()
            return self.__arreglo[pos]
        except IndexError:
            print("Posición no válida")
        except AssertionError:
            print("La lista está vacía")

    
    def primer_elemento(self):
        try:
            assert self.vacia()
            return self.__arreglo[0]
        except AssertionError:
            print("La lista está vacía")

    def ultimo_elemento(self):
        try:
            assert self.vacia()
            return self.__arreglo[self.__ultimo]
        except AssertionError:
            print("La lista está vacía")
    def vacia(self):
        return self.__cantidad == 0
    def lleno(self):
        return self.__cantidad == self.__tamaño
    