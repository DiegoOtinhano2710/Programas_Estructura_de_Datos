class nodo:
    __dato:object
    __izquierda:object
    __derecha:object

    def __init__(self, dato):
        self.__dato = dato
        self.__derecha = None
        self.__izquierda = None

    def getdato(self):
        return self.__dato
    def getizquierda(self):
        return self.__izquierda
    def getderecha(self):
        return self.__derecha
    def setdato(self,xd):
        self.__dato=xd
    def setizq(self,i):
        self.__izquierda = i
    def setder(self,d):
        self.__derecha = d

class arbol:
    __raiz:nodo
    
    def __init__(self):
        self.__raiz = None
    
    def getraiz(self):
        return self.__raiz
    
    def insertar(self,dato,subarbol=None):
        if subarbol is None:
            subarbol = self.__raiz
        if self.__raiz is None:
            self.__raiz = nodo(dato)
            print("Se ingresó como raíz")
            return
        else:
            if dato < subarbol.getdato():
                if subarbol.getizquierda() is None:
                    nuevo_nodo=nodo(dato)
                    subarbol.setizq(nuevo_nodo)
                    return
                else:
                    self.insertar(dato,subarbol.getizquierda())
            elif dato > subarbol.getdato():
                if subarbol.getderecha() is None:
                    nuevo_nodo=nodo(dato)
                    subarbol.setder(nuevo_nodo)
                    return
                else:
                    self.insertar(dato,subarbol.getderecha())
            else:
                print("El elemento ya está en el arbol")
            return
        
    def buscar(self, dato, subarbol):
        if subarbol is None:
            print("Elemento no encontrado")
        else:
            if dato == subarbol.getdato():
                return subarbol             #Devuelve el nodo donde lo encontró
            elif dato < subarbol.getdato():
                subarbol = self.buscar(dato, subarbol.getizquierda())
            else:
                subarbol = self.buscar(dato, subarbol.getderecha())
        return subarbol
    
    def grado(self, dato):          #cantidad de hijos que tiene un nodo del arbol
        nodo = self.buscar(dato, self.__raiz)
        grado=None
        if nodo is not None:    #encontró el nodo con la clave
            if nodo.getizquierda() is not None and nodo.getderecha() is not None:
                grado = 2
            elif nodo.getizquierda() is not None and nodo.getderecha() is None:
                grado = 1
            elif nodo.getizquierda() is None and nodo.getderecha() is not None:
                grado = 1
            else:
                grado=0
        return grado

    def hoja(self, dato):           #evalua si un nodo es hoja
        hoja = self.grado(dato)
        if hoja == 0:
            hoja = True
        else:
            hoja = False
        return hoja
    
    def InOrder(self,subarbol):
        if subarbol is not None:
            self.InOrder(subarbol.getizquierda())
            print(subarbol.getdato(), end='  -  ')
            self.InOrder(subarbol.getderecha())



if __name__=='__main__':
    a = arbol()
    opcion = input('''Elegir opción: 
                   a) Ingresar número
                   b) Mostrar arbol
                   c) Ver si un nodo es hoja
                   z) salir
                   --> ''')
    while opcion != 'z':
        if opcion == 'a':
            num = int(input("Ingresar número: "))
            a.insertar(num)
        elif opcion == 'b':
            a.InOrder(a.getraiz())
            print()
        elif opcion == 'c':
            dato = int(input("Elegir un número para saber si es hoja: "))
            band = a.hoja(dato)
            if band is True:
                print("El nodo perteneciente al dato elegido es hoja en el arbol")
            else:
                print("El nodo perteneciente al dato ingresado, no es hoja en el arbol")
        opcion = input("Elegir opción: ")
