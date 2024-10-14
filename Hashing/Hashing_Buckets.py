import numpy as np
class buckets:
    __tabla:np.ndarray
    __overflow:int
    __cant_claves:np.ndarray
    __dimension:int

    def __init__(self, claves, buckets):
        self.__dimension = (claves/buckets) + 20%(claves/buckets)
        self.__tabla = np.empty((self.__dimension, buckets)) 
        self.__cant_claves = np.zeros(self.__dimension)
        self.__overflow = claves/buckets

    def metodo_division(self, clave, c, b):
        return clave % (c/b)                #hace el modulo con la clave/buckets para que caiga en el area primaria y no en overflow

    def metodo_extraccion(self, clave, c, b):
        clave = str(clave)
        clave = clave[-3:]
        return clave % (c/b)

    def metodo_plegado(self, clave, c, b):
        clave = str(clave)
        total = 0
        for i in range(0, len(clave), 2):
            total += int(clave[i:i+2])
        return total % (c/b)
    
    def metodo_cuadrado_medio(self, clave, c, b):
        clave = str(clave ** 2)
        medio = len(clave) // 2
        if len(clave) % 2 == 0:
            clave = int(clave[medio-1:medio+1])
        else:
            clave = int(clave[medio-1:medio+2])
        return clave % (c/b)
    
    def metodo_ASCII(self, clave, c, b):
        total = 0
        for i in range(len(clave)):
            total += ord(clave[i]) * (2 ** i+1)
        return total % (c/b)
    
    def insertar(self, clave, metodo, c, b):
        if metodo == 'a':
            pos = self.metodo_division(clave, c, b)
        elif metodo == 'b':
            pos = self.metodo_extraccion(clave, c, b)
        elif metodo == 'c':
            pos = self.metodo_plegado(clave, c, b)
        elif metodo == 'd':
            pos = self.metodo_cuadrado_medio(clave, c, b)
        elif metodo == 'e':
            pos = self.metodo_ASCII(clave, c, b)

        if self.__cant_claves[pos] < b:
            self.__tabla[pos, self.__cant_claves[pos]] = clave
            self.__cant_claves[pos] += 1
        else:
            o = self.__overflow
            while self.__cant_claves[o] == b and o != self.__dimension:
                o += 1
            if o == self.__dimension:
                print("No queda espacio en el área de overflow. No se puede insertar")
            else:
                self.__tabla[o, self.__cant_claves[o]] = clave
                self.__cant_claves[o] += 1

    def buscar(self, clave, metodo, c, b):
        if metodo == 'a':
            pos = self.metodo_division(clave)
        elif metodo == 'b':
            pos = self.metodo_extraccion(clave)
        elif metodo == 'c':
            pos = self.metodo_plegado(clave)
        elif metodo == 'd':
            pos = self.metodo_cuadrado_medio(clave)
        elif metodo == 'e':
            pos = self.metodo_ASCII(clave)
        fila =  None
        columna = None
        j=0
        while j < b and self.__tabla[pos,j] != clave:
            j += 1
        if j < b:
            fila = pos
            columna = j
        else:
            o = self.__overflow
            while o < self.__dimension:
                j=0
                while j < b and self.__tabla[o,j] != clave:
                    j += 1
                if j == b:
                    o += 1
                else:
                    fila = o
                    columna = j
                    break
        return fila, columna