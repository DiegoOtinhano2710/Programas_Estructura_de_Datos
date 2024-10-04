import random
class tabla_hashing:
    __tabla: list
    __dimension:int

    def __init__(self, dim):
        self.__tabla = [None] * dim
        self.__dimension = dim
    
    def transf_division(self, clave):
        return clave % self.__dimension
    
    def insertar(self, clave):
        pos = self.transf_division(clave)
        if self.__tabla[pos] is None:
            self.__tabla[pos] = clave
        else:
            while self.__tabla[pos] is not None:
                pos = (pos + 1) % self.__dimension
            self.__tabla[pos] = clave
    
    def mostrar(self):
        for i in range(self.__dimension):
            if self.__tabla[i] is not None:
                print(self.__tabla[i], end='   ')
            else:
                print("N", end='   ')

    def buscar(self,dato):
        i=0
        while i < self.__dimension and self.__tabla[i] != dato:
            i += 1
        if i < self.__dimension:
            print(f"El dato está en la posición {i+1}")
        else:
            print("El dato no está en la tabla")
        
    
def rellenar(tabla):
        for i in range(7):
            num = random.randint(0,100000)
            tabla.insertar(num)
            
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

if __name__ == "__main__":
    opcion=input('''Selccione opcion:
                 a) Tabla sin primo
                 b) Tabla con primo
                 c) Buscar
                 z) salir
                 ---->  ''')
    while opcion != 'z':
        if opcion == 'a':
            cant_claves = int(input("Ingresar cantidad de claves: "))
            tamaño = int(cant_claves // 0.7)
            tabla = tabla_hashing(tamaño)
            rellenar(tabla)
            tabla.mostrar()
        elif opcion == 'b':
            cant_claves = int(input("Ingrese cantidad de claves: "))
            tamaño = int(cant_claves // 0.7)
            #print(tamaño)
            if not es_primo(tamaño):
                tamaño=sig_primo(tamaño)
            #print(tamaño)
            tabla = tabla_hashing(tamaño)
            rellenar(tabla)
            tabla.mostrar()
        elif opcion == 'c':
            dato=int(input("Ingresar dato a buscar: "))
            tabla.buscar(dato)
        print('')
        opcion = input("Seleccione opcion: ")
    
    