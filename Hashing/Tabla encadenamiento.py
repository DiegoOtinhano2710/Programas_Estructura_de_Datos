import string
import random
class nodo:
    __dato:object
    __siguiente:object
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente=None
    def getdato(self):
        return self.__dato
    def getsig(self):
        return self.__siguiente
    def setdato(self,x):
        self.__dato = x
    def setsig(self,x):
        self.__siguiente = x

class hash_encadenamiento:
    __tabla:list
    __dimension:int
    __cant:int

    def __init__(self, dim):
        self.__dimension = dim
        self.__tabla = [None] * self.__dimension
        self.__cant = 0

    def metodo_division(self, clave):
        return clave % self.__dimension
    
    def metodo_extraccion(self, clave):
        clave = str(clave)
        clave = clave[-3:]
        return clave % self.__dimension

    def metodo_plegado(self, clave):
        clave = str(clave)
        total = 0
        for i in range(0, len(clave), 2):
            total += int(clave[i:i+2])
        return total % self.__dimension
    
    def metodo_cuadrado_medio(self, clave):
        clave = str(clave ** 2)
        medio = len(clave) // 2
        if len(clave) % 2 == 0:
            clave = int(clave[medio-1:medio+1])
        else:
            clave = int(clave[medio-1:medio+2])
        return clave % self.__dimension
    
    def metodo_ASCII(self, clave):
        total = 0
        for i in range(len(clave)):
            total += ord(clave[i]) * (2 ** i+1)
        return total % self.__dimension

    def insertar(self, clave, metodo):
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

        if self.__tabla[pos] is None:
            nuevo_nodo = nodo(clave)
            self.__tabla[pos] = nuevo_nodo
        else:
            cabeza = self.__tabla[pos]
            while cabeza.getdato() != clave and cabeza.getsig() is not None:
                cabeza = cabeza.getsig()
            if cabeza.getsig() is not None:
                print("El elemento ya está en la tabla")
            else:
                nuevo_nodo = nodo(clave)
                cabeza.setsig(nuevo_nodo)
    
    def buscar(self, clave, metodo):
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
        encontrado = None
        num = 1
        cabeza = self.__tabla[pos]
        while cabeza is not None:
            if cabeza.getdato() == clave:
                encontrado = pos
                break
            num += 1
            cabeza = cabeza.getsig()
        return encontrado, num
    
    def mostrar(self):
        for i in range(len(self.__tabla)):
            if self.__tabla[i] is None:
                print(f"No hay ninguna clave en la lista perteneciente a la componente {i}")   
            else:
                cabeza = self.__tabla[i]
                print(f"Lista de claves sinónimas para la componente {i}: ", end='  ')
                while cabeza is not None:
                    print(cabeza.getdato(), end='   ')
                    cabeza = cabeza.getsig()
                print()
    
    def itemd(self):
        total = 0
        listas_dentro_del_promedio = 0
        listas_no_vacias = 0
        for i in range(len(self.__tabla)):
            if self.__tabla[i] is not None:
                listas_no_vacias += 1
                cant = self.long_listas(i)
                total += cant
                print(f"El tamaño de la lista de claves sinónimas que está en la componente {i} es {cant}")
        prom = total // listas_no_vacias
        for i in range(len(self.__tabla)):
            if self.__tabla[i] is not None:
                cant = self.long_listas(i)
                if cant >= (prom - 3) and cant <= (prom + 3):
                    listas_dentro_del_promedio += 1
        print(f"La cantidad de listas con una longitud que varía en hasta 3 unidades respecto al promedio ({prom}) de las longitudes es {listas_dentro_del_promedio}.")

    def long_listas(self, componente):
        cant = 0
        cabeza = self.__tabla[componente]
        while cabeza is not None:
            cant += 1
            cabeza = cabeza.getsig()
        return cant
        


def rellenar(tabla, num, opcion):
    llenado = input('''Seleccione cómo quiere rellenar la tabla:
                    a) Ingresar por teclado
                    b) Llenar la tabla automaticamente de forma aleatoria
                    ---->   ''')
    if llenado.lower() == 'a':
        confirmacion = 'si'
        while confirmacion.lower() == 'si':
            if opcion == 'e':
                clave = input("Ingresar clave que desea almacenar: ")
            else:
                clave = int(input("Ingresar clave que desea almacenar: "))
            tabla.insertar(clave, opcion)
            confirmacion = input("¿Quiere ingresar otra clave? si/no:  ")
            while confirmacion != 'si' and confirmacion != 'no':
                confirmacion = input("¿Quiere ingresar otra clave? si/no (Seleccione una respuesta válida):  ")
    elif llenado.lower() == 'b':
        if opcion == 'e':       #esto va a generar claves alfanumericas rando
            digitos = string.ascii_letters + string.digits + string.punctuation         #en digitos almacena todos los "digitos" ASCII
            for _ in range(num):
                clave = ''
                for _ in range(5):                                           #esto es para generar cadenas de 5 caracteres
                    clave += random.choice(digitos)                          #eligiendo caracteres random de "digitos"
                tabla.insertar(clave, opcion)
        else:               
            for _ in range(30):
                clave = random.randint(0,100000)                            #sino, genera claves random de enteros
                tabla.insertar(clave, opcion)


def es_primo(n):
    # Los números menores que 2 no son primos
    if n < 2:
        return False
    # Verifica divisibilidad desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # n es divisible por i, no es primo
    return True  # n es primo

def sig_primo(n):
    """Encuentra el siguiente número primo después de n."""
    siguiente = n + 1
    while True:
        if es_primo(siguiente):
            return siguiente
        siguiente += 1

def submenu(tabla, cant):
    op=input('''Seleccione el método de transformación deseado: 
             a) Método de división
             b) Método de extracción
             c) Método de plegado
             d) Método de cuadrado medio
             e) Método para claves alfanuméricas
             -----> ''')
    if op.lower() == 'a' or op.lower() == 'b' or op.lower() == 'c' or op.lower() =='d' or op.lower() == 'e':
        rellenar(tabla, cant, op)
    else:
        print("Método no válido")
        submenu(tabla, cant)
    return op

if __name__ == "__main__":
    opcion=input('''Selccione opcion:
                 a) Tabla
                 b) Tabla de tamaño primo
                 c) Buscar
                 d) Informar longitud de las listas de claves sinónimas y todo el chiche
                 z) salir
                 ---->  ''')
    while opcion != 'z':
        if opcion.lower() == 'a':
            cant_claves = int(input("Ingresar cantidad de claves: "))
            tamaño = int(cant_claves // 0.7)
            tabla = hash_encadenamiento(tamaño)
            para_buscar = submenu(tabla, tamaño)
            tabla.mostrar()
        elif opcion.lower() == 'b':
            cant_claves = int(input("Ingrese cantidad de claves: "))
            tamaño = int(cant_claves // 0.7)
            #print(tamaño)
            if not es_primo(tamaño):
                tamaño=sig_primo(tamaño)
            #print(tamaño)
            tabla = hash_encadenamiento(tamaño)
            para_buscar = submenu(tabla, tamaño)
            tabla.mostrar()
        elif opcion.lower() == 'c':
            if tabla is None:
                print("Debes crear una tabla primero usando las opciones 'a' o 'b'")
            else:
                if para_buscar == 'e':
                    dato = input("Ingresar dato a buscar: ")
                else:
                    dato=int(input("Ingresar dato a buscar: "))
                componente, pos = tabla.buscar(dato, para_buscar)
                if componente is not None:
                    print(f"El dato se encontró en la lista de la componente {componente}, en la posición {pos}")
                else:
                    print("El dato no se encontró en la tabla")
        elif opcion.lower() == 'd':
            tabla.itemd()
        else:
            print("Opción no válida", end='')
        opcion=input('''\nSelccione opcion:
                 a) Tabla
                 b) Tabla de tamaño primo
                 c) Buscar
                 d) Informar longitud de las listas de claves sinónimas
                 z) salir
                 ---->  ''')
    if opcion.lower() == 'z':
        print("Menú finalizado. Gracias por testearlo <3")
