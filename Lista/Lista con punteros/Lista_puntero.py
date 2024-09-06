import numpy as np
from nodo import nodo
class lista_puntero:
    __maximo:int
    __cab:int
    __cantidad:int
    __espacio:np.ndarray
    __disponible:int

    def __init__(self, xmax):
        self.__maximo=xmax
        self.__cab=0
        self.__cantidad=0
        self.__espacio = np.empty(self.__maximo, dtype=nodo)
        self.__disponible = 0
    
    def vacio(self):
        return self.__cantidad == 0
    
    def getdisponible(self):
        i=0
        while i < self.__maximo and self.__espacio[i].getsiguiente() != None:
            i += 1  #se queda en el nodo con el último dato ingresado
        if i < self.__maximo:
            self.__disponible=i
            return True
        else:
            self.__disponible=-2
            return False
    
    def freedisponible(self):
        if self.__disponible >= 0 and self.__disponible < self.__maximo:
            self.__espacio[self.__disponible].setsiguiente(-2)
            return True
        else:
            return False
    
    def insertar_por_posición(self, dato, posicion):
        if self.__cantidad < self.__maximo and self.__cab >= 0 and self.__cab <= self.__cantidad and self.getdisponible():
            self.__espacio[self.__disponible].setdato(dato)
            anterior=self.__cab
            cabeza=self.__cab
            i=0
            while i < posicion:
                i += 1
                anterior=cabeza
                cabeza=self.__espacio[cabeza].getsiguiente()
            
            if cabeza == self.__cab:        #Inserta al inicio
                if self.__cantidad==0:      #inserta en la lista vacía
                    self.__espacio[self.__cab].setsiguiente(-1)
                else:                       #inserta en la lista con elementos
                    self.__espacio[self.__disponible].setsiguiente(self.__cab)
                self.__cab = self.__disponible
            elif cabeza == -1:              #inserta al final
                self.__espacio[self.__disponible].setsiguiente(-1)
                self.__espacio[anterior].setsiguiente(self.__disponible)
            else:                           #inserta al medio
                self.__espacio[self.__disponible].setsiguiente(cabeza)
                self.__espacio[anterior].setsiguiente(self.__disponible)
            self.__cantidad += 1
            return True
        else:
            print("Espacio lleno o posición incorrecta")
            return False
    
    def insertar_por_contenido(self, dato):
        pass

    def suprimir(self, aux, xpos):
        if self.__cantidad != 0 and 0 <= xpos and xpos < self.__cantidad:
            anterior = self.__cab
            cabeza = self.__cab
            i = 0
            while i < xpos and cabeza != -1 :
                i += 1
                anterior = cabeza
                cabeza = self.__espacio[cabeza].getsiguiente()
            if cabeza == self.__cab:
                if self.__cantidad == 1:
                    self.__cab = 0
                else:
                    self.__cab = self.__espacio[anterior].getsiguiente()
            else:
                self.__espacio[anterior].setsiguiente(self.__espacio[cabeza].getsiguiente())
            aux = self.__espacio[cabeza].getdato()
            self.__disponible = cabeza
            self.freedisponible(self.__disponible)
            self.__cantidad -= 1
        else:
            print("La lista está vacía o se seleccionó una posición incorrecta")
            aux=0


