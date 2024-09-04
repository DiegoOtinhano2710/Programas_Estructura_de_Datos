from classNodo import nodo
class cola_encadenada:
    __primero:nodo
    __ultimo:nodo
    __cant:int

    def __init__(self):
        self.__cant=0
        self.__primero=None
        self.__ultimo=None
    
    def vacio(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        nuevo_nodo=nodo(dato)
        if self.vacio():
            self.__primero = nuevo_nodo
        else:
            self.__ultimo.setsiguiente(nuevo_nodo)      #es insercion al final
        self.__ultimo=nuevo_nodo
        self.__cant += 1

    def eliminar(self):
        if self.vacio():
            print("La cola está vacía")
            aux = None
        else:
            aux=self.__primero.getdato()
            self.__primero=self.__primero.getsiguiente()
            self.__cant -= 1
        return aux
    
    def recorrer(self):
        aux=self.__primero
        if self.vacio():
            print("La cola está vacía")
        else:
            while aux != None:
                print(aux.getdato(), end='  -  ')
                aux=aux.getsiguiente()

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Insertar un número entero")
    print("2. Eliminar el tope de la cola")
    print("3. Recorrer la cola")
    print("4. Salir")

def main():
    cola = cola_encadenada()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            dato = int(input("Ingresa un número entero: "))
            cola.insertar(dato)
            print(f"Número {dato} insertado en la cola.")
        elif opcion == '2':
            eliminado = cola.eliminar()
            if eliminado is not None:
                print(f"Número {eliminado} eliminado de la cola.")
        elif opcion == '3':
            print("Recorriendo la cola:")
            cola.recorrer()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()