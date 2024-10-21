
import numpy as np
class cola():
    __primero : int
    __ultimo : int
    __cantidad : int
    __maximo : int
    __lista : np.ndarray

    def __init__(self, xdim = 10):
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
        adyacentes=[]
        for j in range(self.__vertices):
            if self.__matriz[v,j] == 1:
                adyacentes.append(j+1)
        return adyacentes
    
    def REA(self, s):
        d=[]
        camino = []         #para rastrear el camino
        c=cola()
        for i in range(len(self.__matriz)):
            d.append(None)
            camino.append(None)
        d[s] = 0
        c.insertar(s)
        while not c.vacio():
            v = c.eliminar()
            ady = self.adyacencia(v)        #trae los adyacentes al que suprime de la cola
            for u in ady:
                if d[u] is None:
                    d[u] = d[v] + 1
                    camino[u] = v
                    c.insertar(u)
        return d,camino
    
    def REP(self, s):
        pass
    
    def caminoFloy(self,s):
        pass

                

if __name__=='__main__':
    num=int(input("Ingrese cantidad de vértices del grafo: "))
    m=grafo(num)
    o=input('''Seleccionar opción:
            a) Insertar arista
            b) Mostrar las aristas
            c) Vértices adyacentes a uno ingresado
            d) Camino entre vértices
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
            ady=m.adyacencia(v-1)
            if ady:
                for i in range(len(ady)):
                    print(f"El vértice {ady[i]} es adyacente al vértice {v}")
        elif o=='d':
            s=int(input("Insertar vértice de inicio: "))
            dest=int(input("Insertar nodo destino: "))
            vertices, pred = m.REA(s)
            if vertices[dest-1] is None:
                print(f"No hay camino desde el nodo {s} hasta el nodo {dest}")
            else:
                camino = []
                while dest is not None:
                    camino.append(dest)
                    dest = pred[dest]
                camino.reverse()
                print("El camino más corto es: ", camino)
        else:
            print("Ingrese una opción válida!")
        o=input('''Seleccionar opción:
            a) Insertar arista
            b) Mostrar las aristas
            c) Vértices adyacentes a uno ingresado
            z) Salir
            ----->  ''')
