from Pila_Secuencial import pila as p

def binario():
    pila = p()
    num = int(input("Ingrese número deseado: "))
    while num >= 2:
        resto = num % 2
        num = num // 2
        pila.insertar(resto)
    print(num, end='')
    while not pila.vacio():
        print(pila.eliminar(), end='')
    print()

def factorial():
    num = int(input("Ingrese número deseado: "))
    pila=p(num)
    aux = num
    if num == 0:
        print (f'El factorial de 0 es 1')
    else: 
        while num >= 1:
            pila.insertar(num)
            num -= 1
        num=1
        while not pila.vacio():
            num *= pila.eliminar()
        print (f'El factorial de {aux} es {num}')

if __name__ == '__main__':
    opcion=input('''Elija una opción: 
                 a. Convertir numero en binario
                 b. Factorial
                 d. salir del menú
                 ----> ''')
    while(opcion != 'd'):
        if opcion == 'a':
            binario()
        elif opcion == 'b':
            factorial()
        opcion=input('Elija una opción: ')