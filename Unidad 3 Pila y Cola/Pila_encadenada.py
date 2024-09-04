from classNodo import nodo
class pila_encadenada:
    __cant:int
    __tope:nodo

    def __init__(self):
        self.__cant=0
        self.__tope=None
    
    def vacia(self):
        return self.__cant==0
    
    def insertar(self, dato):   #es una insersión por la cabeza
        nuevo_nodo=nodo(dato)   
        nuevo_nodo.setsiguiente(self.__tope)
        self.__tope=nuevo_nodo
        self.__cant += 1 
    
    def eliminar(self):     #se suprime por la cabeza
        if self.vacia():
            print("La lista está vacía")
            return None
        else:
            aux=self.__tope.getdato()
            self.__tope = self.__tope.getsiguiente()
            self.__cant -= 1
            return aux
        
    def recorrer(self):
        aux=self.__tope
        while aux != None:
            print(aux.getdato(), end='  -  ')
            aux=aux.getsiguiente()

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Insertar un número entero")
    print("2. Eliminar el tope de la pila")
    print("3. Recorrer la pila")
    print("4. Salir")

def main():
    pila = pila_encadenada()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            dato = int(input("Ingresa un número entero: "))
            pila.insertar(dato)
            print(f"Número {dato} insertado en la pila.")
        elif opcion == '2':
            eliminado = pila.eliminar()
            if eliminado is not None:
                print(f"Número {eliminado} eliminado de la pila.")
        elif opcion == '3':
            print("Recorriendo la pila:")
            pila.recorrer()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()