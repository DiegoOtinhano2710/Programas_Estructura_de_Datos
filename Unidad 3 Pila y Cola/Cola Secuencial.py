import numpy as np
class cola():
    __primero : int
    __ultimo : int
    __cantidad : int
    __maximo : int
    __lista : np.ndarray

    def __init__(self, xdim):
        self.__primero=0
        self.__ultimo=0                                  #apunta al ultimo elemento insertado + 1. lo que sería el primer espacio disponible para insertar
        self.__cantidad=0
        self.__maximo = xdim
        self.__lista=np.empty(self.__maximo)
    
    def vacio(self):
        return self.__cantidad == 0
    def lleno(self):
        return self.__cantidad == self.__maximo
    def insertar(self, nuevo):
        if not self.lleno():
            self.__lista[self.__ultimo] = nuevo             #inserta en elemento en el lugar del último
            self.__ultimo = (self.__ultimo + 1) % 10        #hace que el último apunte al que le sigue 
            self.__cantidad += 1
        else:
            print ("La cola está llena")

    def eliminar(self):
        if self.vacio():
            print("La cola está vacía")
        else:
            x = self.__lista[self.__primero]
            self.__primero = (self.__primero + 1) % 10      #hace que apunte al que le sigue al primero
            self.__cantidad -= 1
        return x
    
    def recorrer(self):
        if self.vacio():
            print("La cola está vacía")
        else:
            aux = self.__primero
            x = self.__lista[aux]
            aux = (aux + 1) % 10      #hace que apunte al que le sigue al primero
        return x
    
    