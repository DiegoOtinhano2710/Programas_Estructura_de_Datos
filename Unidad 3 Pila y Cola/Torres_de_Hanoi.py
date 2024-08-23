from Pila_Secuencial import pila as p

def inicializarA(torreA, dimension):
    for i in range(dimension):
        torreA.insertar(dimension)
        dimension -= 1

def meteYsaca(torreX, discoelegido):
    if torreX.vacio():
        aux=discoelegido + 1
    else:
        aux=torreX.eliminar()
        torreX.insertar(aux)
    return aux

if __name__=='__main__':
    cant_discos=int(input("Ingrese la cantidad de discos con los que desea jugar: "))
    torreA = p(cant_discos)
    torreB = p(cant_discos)
    torreC = p(cant_discos)
    controlador=False
    inicializarA(torreA, cant_discos)
    num_movimientos=0
    while not torreC.lleno():
        inicial=input("Elegir torre de donde quiere retirar disco: \nA. Torre Inicial.\nB. Torre Intermedia.\nC. Torre Final.\n---> ")
        if inicial.upper()=='A' and not torreA.vacio():
            disco_elegido=torreA.eliminar()
            controlador=True
        elif inicial.upper()=='B' and not torreB.vacio():
            disco_elegido=torreB.eliminar()
            controlador=True
        elif inicial.upper()=='C' and not torreC.vacio():
            disco_elegido=torreC.eliminar()
            controlador=True
        else:
            print("Error al seleccionar torre.")
        while controlador == True:
                destino=input("Elegir torre en la que quiera insertar el disco: \nA. Torre Inicial.\nB. Torre Intermedia.\nC. Torre Final.\n---> ")
                if destino.upper() == 'A' and disco_elegido < meteYsaca(torreA, disco_elegido):
                    torreA.insertar(disco_elegido)
                    controlador = False
                    num_movimientos += 1
                elif destino.upper() == 'B' and disco_elegido < meteYsaca(torreB, disco_elegido):
                    torreB.insertar(disco_elegido)
                    controlador = False
                    num_movimientos += 1
                elif destino.upper() == 'C' and disco_elegido < meteYsaca(torreC, disco_elegido):
                    torreC.insertar(disco_elegido)
                    controlador = False
                    num_movimientos += 1
                else:
                    print("Error al seleccionar torre destino.")
    print(f"Felicidades, has ganado el juego de las Torres de Hanoi con {cant_discos} discos en {num_movimientos} movimientos")