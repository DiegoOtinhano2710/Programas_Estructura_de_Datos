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
        if subarbol is not None:
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

    def nivel(self, dato):
        nodo = self.buscar(dato, self.__raiz)
        nivel = None
        if nodo is not None:
            nivel = 1
            subarbol = self.__raiz
            while subarbol.getdato() != dato:
                nivel += 1
                if dato < subarbol.getdato():
                    subarbol = subarbol.getizquierda()
                else:
                    subarbol = subarbol.getderecha()
        return nivel
    
    def getInfimo(self,subarbol):
        subarbol= subarbol.getizquierda()
        while self.grado(subarbol.getdato()) != 0:
            subarbol= subarbol.getderecha()
        return subarbol

    def getPadre(self,clave):
        nodo= self.__raiz
        nivel= self.nivel(clave)
        nivel_actual= 1
        if clave != nodo.getdato():
            while nivel_actual != nivel-1:
                if clave > nodo.getdato():
                    nodo= nodo.getderecha()
                else:
                    nodo= nodo.getizquierda()
                nivel_actual+=1
        else:
            nodo = None
        return nodo

    def suprimir(self,clave): #Es mas facil hacer el seguimiento viendo la imagen de la carpeta y ejecutandolo
        subarbol= self.buscar(self.__raiz,clave)
        padre= self.getPadre(clave)

        if subarbol is not None:
            grado= self.grado(clave)
            if grado == 0: #Si el grado es 0, es un nodo hoja. Ahora el padre va a apuntar a None en su rama derecha/izquierda en la que estaba el hijo suprimido
                if clave > padre.getdato():
                    padre.setder(None)
                else:
                    padre.setSAI(None)
            if grado == 1: #Si el grado es 1, el nodo tenia un hijo. Ahora el padre deberá apuntar a ese hijo
                if subarbol.getderecha() is not None: #Busco el hijo (esta en la derecha O izquierda, ya que solo tiene 1)
                    hijo= subarbol.getderecha()
                else:
                    hijo= subarbol.getIzquierda()

                subarbol.setdato(hijo.getdato()) #Ahora el nodo a suprimir será una copia de su hijo
                subarbol.setderecha(hijo.getderecha())
                subarbol.setizquierda(hijo.getizquierda())

                #if subarbol.getDerecha().getDato() == subarbol.getDato():
                #    subarbol.setSAD(None)
                #else:
                #    subarbol.setSAD(None)
            if grado== 2: #Si el grado es 2, hay que buscar el infimo o el supremo para reemplazarlo
                infimo=self.getInfimo(subarbol)
                padre_infimo= self.getPadre(infimo.getdato())
                subarbol.setdato(infimo.getdato())

                if infimo.getdato() > padre_infimo.getdato():
                    padre_infimo.setder(None)
                else:
                    padre_infimo.setizq(None)

    def hijo(self,padre,hijo):
        subarbol_padre= self.buscar(self.__raiz,padre)
        subarbol_hijo= self.buscar(self.__raiz,hijo)
        es_hijo= False
        if subarbol_hijo is not None and subarbol_padre is not None:
            es_hijo= subarbol_padre.getizquierda()==subarbol_hijo or subarbol_padre.getderecha()==subarbol_hijo
        return es_hijo

    def padre(self,padre,hijo):
        subarbol_padre= self.buscar(self.__raiz,padre)
        subarbol_hijo= self.buscar(self.__raiz,hijo)
        es_padre= False
        if subarbol_padre is not None and subarbol_hijo is not None:
            nodo= self.__raiz
            nivel= self.nivel(hijo)
            nivel_actual= 1
            if hijo != nodo.getdato():
                while nivel_actual != nivel-1:
                    if hijo > nodo.getdato():
                        nodo= nodo.getderecha()
                    else:
                        nodo= nodo.getizquierda()
                    nivel_actual+=1
                es_padre = nodo==subarbol_padre
            else:
                print("Ingresaste la raiz. No tiene padre")
        return es_padre
    
    def altura(self,subarbol,maximo=1):
        if subarbol is not None:
            nivel = self.nivel(subarbol.getdato())
            if nivel > maximo:
                maximo = nivel
            maximo = self.altura(subarbol.getizquierda(), maximo) #Voy a recorrer todos los de la izqueirda
            maximo = self.altura(subarbol.getderecha(), maximo) #Luego todos los de la derecha
        return maximo

    def PreOrden(self,subarbol):
        if subarbol is not None:
            print(subarbol.getdato())
            self.InOrder(subarbol.getizquierda())
            self.InOrder(subarbol.getderecha())

    def PostOrden(self,subarbol):
        if subarbol is not None:
            self.InOrder(subarbol.getizquierda())
            self.InOrder(subarbol.getderecha())
            print(subarbol.getdato())

    def camino(self,origen,destino):
        subarbol_origen= self.buscar(self.__raiz,origen)
        camino="° "
        if subarbol_origen is not None: #Reviso que el nodo origen exista
            subarbol_destino= self.buscar(subarbol_origen,destino) #Reviso que el nodo destino exista en los descendientes del arbol origen
            subarbol= subarbol_origen
            if subarbol_destino is not None: #Empezare a concatenar el contenido de los nodos como un camino en un string
                while subarbol.getdato() != destino:
                    if destino > subarbol.getdato():
                        camino+= str(subarbol.getdato())+ " -> "
                        subarbol= subarbol.getderecha()
                    else:
                        camino+= str(subarbol.getdato())+ " -> "
                        subarbol= subarbol.getizquierda()
                camino+= str(subarbol.getdato())+ " -|"
            else:
                print(f"ERROR. El nodo origen {subarbol.getdato()} no es antecesor de {destino}")
        return camino
    
def hermano(padre, hijo, arbol):
    hijo = arbol.buscar(hijo, arbol.getraiz())
    hermano = None
    if hijo.getdato() < padre.getdato():
        hermano = padre.getderecha()
    else:
        hermano = padre.getizquierda()
    return hermano

def contarnodos(subarbol):
    if subarbol is None:
        return 0
    else:
        return 1 + contarnodos(subarbol.getizquierda()) + contarnodos(subarbol.getderecha())

def altura(subarbol, altura = None, max=0):
    if subarbol is not None:
        altura = subarbol.nivel(subarbol.getdato())
        if altura > max:
            max = altura
        altura(subarbol.getizquierda(), None, max)
        altura(subarbol.getderecha(), None, max)

if __name__=='__main__':
    a = arbol()
    opcion = input('''Elegir opción: 
                   0) Ingresar dato
                   a) Nodo padre y hermano
                   b) Mostrar cantidad de nodos
                   c) mostrar altura
                   d) mostrar sucesores de un nodo
                   z) salir
                   --> ''')
    while opcion != 'z':
        if opcion == 'a':
            num = int(input("Ingresar número de nodo: "))
            hijo = a.buscar(num, a.getraiz())
            if hijo is not None:
                padre = a.getPadre(num)
                if padre is not None:
                    hermano = hermano(padre, hijo, a)
                    if hermano is not None:
                        print(f"El nodo ingresado tiene un padre: {padre} y tiene un hermano: {hermano}")
                    else:
                        print(f"El nodo ingresado tiene un padre: {padre} y NO tiene hermano")
                else:
                    print("El nodo no tiene padre, es la raiz")
            else:
                print("El nodo no se encontró en el árbol")
        elif opcion == 'b':
            contarnodos(a.getraiz())
        elif opcion == 'c':
            altura(a.getraiz())
        elif opcion == 'd':
            dato = int(input("Ingresar código del nodo: "))
            nodo_raiz = a.buscar(dato, a.getraiz())
            if nodo_raiz is not None:
                if nodo_raiz.getderecha() is None and nodo_raiz.getizquierda() is None:
                    print("El nodo ingresado no tiene sucesores")
                else:
                    if nodo_raiz.getizquierda() is not None:
                        a.InOrder(nodo_raiz.getizquierda())
                    if nodo_raiz.getderecha() is not None:
                        a.InOrder(nodo_raiz.getderecha())
            else:
                print("El nodo ingresado no está en el árbol")
        opcion = input("Elegir opción: ")
