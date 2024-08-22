def traspaso(A: list)-> list: # Toma una matriz y entrega la matriz transpuesta
    # Se inicializan y declaran las variables locales
    fila : list = []
    i : int = 0
    j : int = 0

    # Se itera pasando primero por cada fila y después por cada columna.
    for j in range(len(A[i])):
        for i in range(len(A)):
            fila.append(A[i][j]) # Se agrega el elemento de una misma columna pero en distintas filas
        B.append(fila) # Al finalizar se añade la fila transpuesta a la matriz resultante
        fila = [] # Se actualiza la fila y se elimina sus contenidos para la próxima iteración
    return B # Se retorna la matriz transpuesta

# Se imprime la matriz transpuesta
def imprimirMatriz(B: list)-> list:
  print("La matriz resultante es:")
  for i in range(len(B)): print(B[i])

if __name__ == "__main__": # Función main para dar inicio al código
    # Se inicializan y declaran variables globales
    A : list = [[6,-1,-5,2],[3,-2,4,0]]
    B : list = []

    # Se obtiene la matriz transpuesta y se imprime
    B = traspaso(A)
    imprimirMatriz(B)