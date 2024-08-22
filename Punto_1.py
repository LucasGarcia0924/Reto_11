def comprobar (A:list, B:list ) -> bool: # Al recibir ambas listas las compara y verifica si son operables o no
    for i in range(len(A)): # Recorre filas
        for j in range(len(A[i])): # Recorre cada columna
            if len(A[i]) != len(B[i]): # Si no coincide alguna longitud no son operables
                return False
    return True # Si todas las longitudes coinciden es operable

def operar (A:list, B:list ) -> list: # Toma las dos matrices iniciales y devuelve la final
    fils : list = [] # Se crea la lista de filas para rellenarla una a una en cada iteración
    option = str(input("deseas: 'sumar' o 'restar'")) # Se elige entre operaciones
    for i in range(len(A)): # Recorre filas
        for j in range(len(A[i])): # Recorre columnas
            
            #Se suma o resta cada valor, o sino se vuelve a elegir entre la operación
            if option == "sumar":
                valor = A[i][j] + B[i][j]
                fils.append(valor)
            elif option  == "restar":
                valor = A[i][j] - B[i][j]
                fils.append(valor)
            else:
                print("Argumento erróneo")
                return operar(A,B)
        # Se agrega a la lista final cada fila de la matriz hasta completarla
        C.append(fils)
        fils = [] # Se actualiza la variable
    return C # Se retorna la matriz completa

def imprimirMatriz(C: list): # Se imprime la matriz resultante
  print("La matriz resultante es:")
  for i in range(len(C)): print(C[i])

if __name__ == "__main__": # Función main para iniciar el código
    # Se declaran e inicializan las variables
    A : list = [[1,2],[4,5],[8,9]]
    B : list = [[9,8],[6,5],[3,2]]
    C : list = []
    Semejanza: bool = comprobar(A,B)

    # Se valida la capacidad de operar las matrices, y si es posible, se entrega el resultado
    if Semejanza == True: 
        print("Es posible sumar y restar estas matrices")
        C = operar(A,B)
        imprimirMatriz(C)
    else:
        print("No es posible sumar ni restar estas matrices")
