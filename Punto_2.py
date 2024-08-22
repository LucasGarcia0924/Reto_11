def comprobar (A:list, B:list ) -> bool: # Se ingresan las dos funciones y se comprueba su capacidad de multiplicarse
    if len(A[0]) != len(B): # Si la cantidad de filas de A es distinta a la de columnas de B, no son multiplicables
        return False
    return True # En caso de que las longitudes sean congruentes, se valida la condición

def operar(A: list, B: list) -> list: # Se ingresan ambas matrices iniciales y se entrega la resultante
    # Se declara e incializa la matriz resultante
    C : list = []
    
    # Iteramos sobre cada fila en A
    for i in range(len(A)):
        # Fila actual en C
        fila : list = []
        # Iteramos sobre cada columna en B
        for j in range(len(B[0])):
            acumulado : int = 0
            # Sumamos los productos correspondientes
            for k in range(len(A[i])):
                acumulado += A[i][k] * B[k][j]
            # Almacenamos el resultado en la fila correspondiente
            fila.append(acumulado)
        # Añadimos la fila resultado a la matriz C
        C.append(fila)
    
    return C # Entrega la matriz resultante

def imprimirMatriz(C: list): # Imprime la matriz resultante
  print("La matriz resultante es:")
  for i in range(len(C)): print(C[i])

if __name__ == "__main__": # Función main para iniciar el código
    # Se declaran e inicializan las variables
    A : list = [[6,-1,-5,2],[3,-2,4,0]]
    B : list = [[6,2,8],[2,-3,5],[0,-2,3],[4,5,1]]
    C : list = []

    # Se evalua la semejanza y si es posible se operan las matrices y se imprime el resultado
    Semejanza: bool = comprobar(A,B)
    if Semejanza == True:
        print("Es posible multiplicar estas matrices")
        C = operar(A,B)
        imprimirMatriz(C)
    else:
        print("No es posible multiplicar estas matrices")