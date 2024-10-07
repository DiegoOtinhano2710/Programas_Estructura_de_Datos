import random
import string
class tabla_hashing:
    __tabla: list
    __dimension:int
    __cant:int

    def __init__(self, dim):
        self.__tabla = [None] * dim
        self.__dimension = dim
        self.__cant = 0

    def lleno(self):
        return self.__cant == self.__dimension
    
    def metodo_division(self, clave):
        return clave % self.__dimension
    
    def metodo_extraccion(self, clave):
        clave = str(clave)
        clave = clave[-3:]          #toma los últimos 3 dígitos
        return int(clave) % self.__dimension    #hace el metodo de division con esos 3 digitos

    def metodo_plegado(self, clave):
        clave = str(clave)
        pares = []
        for i in range(0, len(clave), 2):
            pares.append(int(clave[i:i+2]))     #crea pares de numeros y los almacena
        suma = sum(pares)
        return suma % self.__dimension

    def metodo_cuadrado_medio(self, clave):
        clave = str(clave ** 2)
        medio = len(clave) // 2
        if len(clave) % 2 == 0:              #la clave tiene cantidad par de digitos
            grupo = clave[medio-1 : medio+1] #toma los pares desde la mitad-1 hasta la mitad+1 pero como excluye a este ultimo toma solo el medio-1 y medio
        else:                                #si la longitud es impar se toman 3 numeros (el del medio y uno a cada lado)
            grupo = clave[medio-1 : medio+2] #toma el grupo desde medio-1 hasta medio+2 para incluir el que le sigue al del medio tmb
        return int(grupo) % self.__dimension

    def metodo_ASCII(self, clave):
        total = 0
        for i in range(len(clave)):
            total += ord(clave[i]) * (2 ** (i+1))
        return total % self.__dimension

    def insertar(self, clave, metodo):
        if self.lleno():
            print("La tabla está llena")
        else:
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
                self.__tabla[pos] = clave
            else:
                while self.__tabla[pos] is not None:
                    pos = (pos + 1) % self.__dimension
                self.__tabla[pos] = clave
            self.__cant += 1
    
    def mostrar(self):
        for i in range(self.__dimension):
            if self.__tabla[i] is not None:
                print(self.__tabla[i], end='   ')
            else:
                print("N", end='   ')

    def buscar(self,clave,metodo):
        longitud_secuencia = 0
        encontrado = None
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
        posición_inicio = pos
        if self.__tabla[pos] == clave:
            encontrado = pos
        else:
            while self.__tabla[pos] != clave:
                pos = (pos + 1) % self.__dimension
                longitud_secuencia += 1
                if pos == posición_inicio:  #si llega a la posicion inicial es porque dio vuelta todo el arreglo
                    break                   #si eso pasa, sale del while con el break
            if self.__tabla[pos] == clave:
                encontrado = pos
                longitud_secuencia += 1
        return encontrado, longitud_secuencia

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
            for _ in range(num):
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
                 z) salir
                 ---->  ''')
    while opcion != 'z':
        if opcion.lower() == 'a':
            cant_claves = int(input("Ingresar cantidad de claves: "))
            tamaño = int(cant_claves // 0.7)
            tabla = tabla_hashing(tamaño)
            para_buscar = submenu(tabla, cant_claves)
            tabla.mostrar()
        elif opcion.lower() == 'b':
            cant_claves = int(input("Ingrese cantidad de claves: "))
            tamaño = int(cant_claves // 0.7)
            #print(tamaño)
            if not es_primo(tamaño):
                tamaño=sig_primo(tamaño)
            #print(tamaño)
            tabla = tabla_hashing(tamaño)
            para_buscar = submenu(tabla, cant_claves)
            tabla.mostrar()
        elif opcion.lower() == 'c':
            if tabla is None:
                print("Debes crear una tabla primero usando las opciones 'a' o 'b'")
            else:
                if para_buscar == 'e':
                    dato = input("Ingresar dato a buscar: ")
                else:
                    dato=int(input("Ingresar dato a buscar: "))
                posición, long = tabla.buscar(dato, para_buscar)
                if posición is not None:
                    print(f"El dato se encontró en la posición {posición + 1}")
                else:
                    print("El dato no se encontró en la tabla")
                print(f"La longitud de secuencia fue: {long}", end='')
        else:
            print("Opción no válida", end='')
        opcion=input('''\nSelccione opcion:
                 a) Tabla
                 b) Tabla de tamaño primo
                 c) Buscar
                 z) salir
                 ---->  ''')
    if opcion.lower() == 'z':
        print("Menú finalizado. Gracias por testearlo <3")
    