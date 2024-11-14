class estación:
    __matriz: list
    __estaciones: int
    __memo: dict  # Diccionario para memorización

    def __init__(self, n):
        self.__estaciones = n
        self.__matriz = []
        for _ in range(n):
            self.__matriz.append([0] * n)
        self.__memo = {}  # Inicializamos el diccionario de memorización
        
    def agregar(self, origen, destino, tiempo):
        self.__matriz[origen-1][destino-1] = tiempo
        self.__matriz[destino-1][origen-1] = tiempo
    
    def mostrar(self):
        print("Conexiones: ")
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz)):
                if self.__matriz[i][j] > 0:
                    print(f"Desde la estación {i+1} hasta la estación {j+1} se demora {self.__matriz[i][j]} minutos")
    
    def Buscar_camino(self, origen, destino, visitados):
        # Crear una clave única para este estado
        clave = (origen, destino, tuple(visitados))
        '''Usamos una tupla porque:
        . Es inmutable, lo que la hace perfecta para ser usada como clave en un diccionario
        . Nos permite agrupar varios valores relacionados en una sola estructura
        . Diccionario: Un diccionario es una estructura de datos que almacena pares de clave-valor. En el código lo usamos así:'''
        # Si ya hemos calculado este clave antes, retornamos el resultado memorizado
        if clave in self.__memo:
            return self.__memo[clave]
        # Caso base: si llegamos al destino
        if origen == destino:
            return 0, [destino + 1]
        min_tiempo = float('inf')
        mejor_camino = None
        # Probamos todas las posibles siguientes estaciones
        for siguiente in range(self.__estaciones):
            if self.__matriz[origen][siguiente] > 0 and not visitados[siguiente]:
                # Marcamos la estación como visitada
                visitados[siguiente] = True
    
                # Llamada recursiva
                tiempo_resto, camino_resto = self.Buscar_camino(siguiente, destino, visitados.copy())
                
                # Si encontramos un camino válido
                if tiempo_resto != float('inf'):
                    tiempo_total = self.__matriz[origen][siguiente] + tiempo_resto
                    if tiempo_total < min_tiempo:
                        min_tiempo = tiempo_total
                        mejor_camino = [origen + 1] + camino_resto
                
                # Desmarcamos la estación
                visitados[siguiente] = False
        
        # Memorizamos el resultado antes de retornarlo
        self.__memo[clave] = (min_tiempo, mejor_camino if mejor_camino else None)
        return self.__memo[clave]
    
    def Camino_PD(self, ori, dest):
        # Reiniciamos la memorización para cada nueva búsqueda
        self.__memo = {}
        visitados = [False] * self.__estaciones
        visitados[ori-1] = True
        
        tiempo, camino = self.Buscar_camino(ori-1, dest-1, visitados)
        
        if tiempo == float('inf'):
            return None, None
        return tiempo, camino

if __name__ == "__main__":
    # Creamos grafo con 6 estaciones
    grafo = estación(6)   
    # Conexiones desde estación 1
    grafo.agregar(1, 2, 30)  # 1 -> 2: 30 min
    grafo.agregar(1, 3, 45)  # 1 -> 3: 45 min
    grafo.agregar(1, 4, 85)  # 1 -> 4: 85 min
    # Conexiones desde estación 2
    grafo.agregar(2, 3, 25)  # 2 -> 3: 25 min
    grafo.agregar(2, 4, 40)  # 2 -> 4: 40 min
    grafo.agregar(2, 5, 75)  # 2 -> 5: 75 min
    # Conexiones desde estación 3
    grafo.agregar(3, 4, 30)  # 3 -> 4: 30 min
    grafo.agregar(3, 5, 55)  # 3 -> 5: 55 min
    # Conexiones desde estación 4
    grafo.agregar(4, 5, 35)  # 4 -> 5: 35 min
    grafo.agregar(4, 6, 50)  # 4 -> 6: 50 min
    # Conexiones desde estación 5
    grafo.agregar(5, 6, 25)  # 5 -> 6: 25 min
    tiempo, camino = grafo.Camino_PD(1, 6)    
    if tiempo is not None:
        print(f"\nRESULTADO FINAL:")
        print(f"Tiempo total: {tiempo} minutos")
        print(f"Ruta: {' -> '.join(map(str, camino))}")
    else:
        print("\nNo se encontró un camino válido entre las estaciones especificadas")