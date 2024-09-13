import numpy as np
class pila():
    __dimension: int        #tamaño de la lista numpy
    __cantidad: int         #cantidad de elementos
    __tope: int             #el tope apunta al ultimo elemento ingresado
    __lista: np.ndarray

    def __init__(self, xdim=10):
        self.__dimension = xdim
        self.__cantidad = 0
        self.__tope = -1    #se pone el tope en -1 para que apunte siempre a uno menos que la cantidad y por 
                            #consecuente al ultimo ingresado
        self.__lista = np.empty(self.__dimension)

    def vacio(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == self.__dimension
    
    def insertar(self, nuevo):
        if self.lleno():
            print("La pila está llena. No se pueden insertar más elementos")
        else:
            self.__tope += 1        #el tope ahora apunta a la siguiente componente (vacia se supone)
            self.__lista[self.__tope] = nuevo #mete el elemento en esa componente
            self.__cantidad += 1
    
    def eliminar(self):
        if self.vacio():
            print("La pila está vacía ya")
        else:
            aux = self.__lista[self.__tope]
            self.__tope -= 1
            self.__cantidad -= 1
            return int(aux)
    
    def recorrer(self):
        aux=self.__tope
        for i in range(self.__cantidad):
            print(self.__lista[aux])
            aux -= 1
