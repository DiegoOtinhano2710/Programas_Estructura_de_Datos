class nodo:
    __dato:object
    __siguiente:object

    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None

    def setsiguiente(self,nodo_siguiente):
        self.__siguiente = nodo_siguiente
    
    def setdato(self, nuevodato):
        self.__dato=nuevodato

    def getsiguiente(self):
        return self.__siguiente
    
    def getdato(self):
        return self.__dato