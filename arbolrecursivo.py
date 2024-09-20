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
    
    def insertar(self,dato,actual=None):
        if actual == None:
            actual = self.__raiz
        if self.__raiz == None:
            self.__raiz = nodo(dato)
            print("Se ingresó como raíz")
            return
        if dato < actual.getdato():
            if actual.getizquierda() == None:
                nuevo_nodo=nodo(dato)
                actual.setizq(nuevo_nodo)
                return
            else:
                self.insertar(dato,actual=actual.getizquierda())
        elif dato > actual.getdato():
            if actual.getderecha() == None:
                nuevo_nodo=nodo(dato)
                actual.setder(nuevo_nodo)
                return
            else:
                self.insertar(dato,actual=actual.getderecha())
        else:
            print("El elemento ya está en el arbol")
            return
        
if __name__=='__main__':
    a = arbol()
    opcion = input("Quiere ingresar numero?")
    while opcion == 'si':
        x = int(input("Ingresar un número: "))
        a.insertar(x)
        opcion = input("Quiere ingresar numero?")
