import numpy as np
class grafo:
    __vertices:int
    __matriz:np.ndarray
    
    def __init__(self,v):
        self.__vertices = v
        self.__matriz=np.zeros((self.__vertices,self.__vertices))
    
    def cargar_arista(self,v1,v2):
        try:
            if v1 < self.__vertices and v2 < self.__vertices:
                pass
            else:
                raise IndexError
        except IndexError:
            print("Índice fuera de rango")


if __name__=='__main__':
    m=grafo(5)
    v1=int(input("Ingresar el primer vértice: "))
    v2=int(input("Ingresar el otro vértice a conectar: "))
    m.cargar_arista(v1,v2)
