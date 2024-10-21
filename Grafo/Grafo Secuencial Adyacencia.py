import numpy as np
class grafo:
    __vertices:int
    __matriz:np.ndarray
    
    def __init__(self,v):
        self.__vertices = v
        self.__matriz=np.zeros((self.__vertices,self.__vertices))
    
    def cargar_arista(self,v1,v2):
        if v1 < self.__vertices and v2 < self.__vertices:
            if self.__matriz[v1,v2] == 0:
                self.__matriz[v1,v2] = 1
                self.__matriz[v2,v1] = 1
            else:
                print("Las aristas ya están cargadas en la matriz")
    
    def mostrar(self):
        print("Matriz de Adyacencia:")
        print("   ", end="")
        for i in range(self.__vertices):
            print(f"{i+1:3}", end="")       #printea el numero de columnas
        print()
        for i in range(self.__vertices):
            print(f"{i+1:3}", end="")       #printea, por fila, el número correspondiente a ella
            for j in range(self.__vertices):    
                print(f"{int(self.__matriz[i, j]):3}", end="")  #printea el valor de cada componente de la matriz
            print()
    
    def adyacencia(self,v):
        cant = 0
        encontrado = False
        for j in range(self.__vertices):
            if self.__matriz[v,j] == 1:
                encontrado=True
                print(f"El vértice {v+1} es adyacente al vértice {j+1}")
        if not encontrado:
            print(f"El vértice {v+1} no tíene vértices adyacentes")


if __name__=='__main__':
    num=int(input("Ingrese cantidad de vértices del grafo: "))
    m=grafo(num)
    o=input('''Seleccionar opción:
            a) Insertar arista
            b) Mostrar las aristas
            c) Vértices adyacentes a uno ingresado
            z) Salir
            ----->  ''')
    while o != 'z':
        if o.lower() == 'a':
            v1=int(input("Ingresar el primer vértice: "))
            v2=int(input("Ingresar el otro vértice a conectar: "))
            if 0 < v1 <= num and 0 < v2 <= num:
                m.cargar_arista(v1-1,v2-1)
            else:
                print("Índice fuera de rango")
        elif o == 'b':
            m.mostrar()
        elif o == 'c':
            v=int(input(f"Ingresar vértice (desde 1 hasta {num}): "))
            m.adyacencia(v-1)
        o=input('''Seleccionar opción:
            a) Insertar arista
            b) Mostrar las aristas
            c) Vértices adyacentes a uno ingresado
            z) Salir
            ----->  ''')
