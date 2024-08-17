import numpy as np
class pila():
    __dimension: int        #tamaño de la lista numpy
    __incremento: int       #en caso de estar llena ya la lista, se incrementa
    __cantidad: int         #cantidad de elementos
    __tope: int             #el tope apunta al ultimo elemento ingresado
    __lista: np.ndarray

    def __init__(self):
        self.__dimension = 20
        self.__incremento = 5
        self.__cantidad = 0
        self.__tope = -1    #se pone el tope en -1 para que apunte siempre a uno menos que la cantidad y por 
                            #consecuente al ultimo ingresado
        self.__lista = np.empty(self.__dimension)

    def vacio(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == self.__dimension
    
    def insertar(self, nuevo):
        if self.lleno():
            print("La pila está llena. No se pueden insertar más elementos")
        else:
            self.__tope += 1        #el tope ahora apunta a la siguiente componente (vacia se supone)
            self.__lista[self.__tope] = nuevo #mete el elemento en esa componente
            self.__cantidad += 1
    
    def eliminar(self):
        if self.vacio():
            print("La pila está vacía ya")
        else:
            aux = self.__lista[self.__tope]
            self.__tope -= 1
            self.__cantidad -= 1
            return int(aux)
    
    def recorrer(self):
        aux=self.__tope
        for i in range(self.__cantidad):
            print(self.__lista[aux])
            aux -= 1
    
    def binario(self):
        num = int(input("Ingrese número deseado: "))
        while num != 0:
            resto = num % 2
            num = num // 2
            self.insertar(resto)
        numero_binario = ''         #esto es pa que no lo muestre uno abajo del otro :P
        while self.__tope > -1:
            numero_binario += str(self.eliminar())
        print(numero_binario)

    def factorial(self):
        num = int(input("Ingrese número deseado: "))
        aux = num
        while num > 1:
            self.insertar(num)
            num -= 1
        while self.__tope > -1:
            num *= self.eliminar()
        print (f'El factorial de {aux} es {num}')

if __name__ == '__main__':
    p=pila()
    opcion=input('''Elija una opción: 
                 a. Convertir numero en binario
                 b. Factorial
                 c. Torres de Hanoi
                 d. salir del menú
                 ----> ''')
    while(opcion != 'd'):
        if opcion == 'a':
            p.binario()
        elif opcion == 'b':
            p.factorial()
        elif opcion == 'c':
            pass
        elif opcion == 'z':
            p.recorrer()
        opcion=input('Elija una opción: ')