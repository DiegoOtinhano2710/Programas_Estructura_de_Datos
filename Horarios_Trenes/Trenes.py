class estación:
    __matriz: list
    __estaciones: int
    __memo: dict

    def __init__(self, n):
        self.__estaciones = n
        self.__matriz = []
        for _ in range(n):
            self.__matriz.append([0] * n)
        self.__memo = {}
        
    def agregar(self, origen, destino, tiempo):
        self.__matriz[origen-1][destino-1] = tiempo
        self.__matriz[destino-1][origen-1] = tiempo
       
    def Buscar_camino(self, origen, destino, visitados):
        # Crear una clave única para este estado
        clave = (origen, destino, tuple(visitados))
        # Busca la clave en el diccionario. Retorna el valor si lo encuentra
        if clave in self.__memo:
            return self.__memo[clave]
        # Caso base
        if origen == destino:
            return 0, [destino + 1]
        min_tiempo = float('inf')
        mejor_camino = None
        # Probamos todas las posibles siguientes estaciones
        for i in range(self.__estaciones):
            if self.__matriz[origen][i] > 0 and not visitados[i]:
                # Marcamos la estación como visitada
                visitados[i] = True
    
                # Llamada recursiva
                tiempo_resto, camino_resto = self.Buscar_camino(i, destino, visitados.copy())
                
                # Si encontramos un camino válido
                if tiempo_resto != float('inf'):
                    tiempo_total = self.__matriz[origen][i] + tiempo_resto
                    if tiempo_total < min_tiempo:
                        min_tiempo = tiempo_total
                        mejor_camino = [origen + 1] + camino_resto
                
                # Desmarcamos la estación
                visitados[i] = False
        
        # Memoizamos el resultado antes de retornarlo
        self.__memo[clave] = (min_tiempo, mejor_camino if mejor_camino else None)
        return self.__memo[clave]
    
    def Camino_PD(self, ori, dest):
        self.__memo = {}
        visitados = [False] * self.__estaciones
        visitados[ori-1] = True
        
        tiempo, camino = self.Buscar_camino(ori-1, dest-1, visitados)
        
        if tiempo == float('inf'):
            return None, None
        return tiempo, camino

if __name__ == "__main__":
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