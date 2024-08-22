def sumaDeFilas(A: list)-> int:# Al ingresar la matriz devuelve el valor entero de la suma de los elementos de una fila
    # Se declaran e inicializan las variables locales
    i = int(input("¿Qué número de fila deseas sumar?"))
    k : int = 0
    j : int = 0
    acumulado: int = 0

    # Si la dila elegida es mayor a las existentes, o se ingresa un valor negativo, se vuelve a la elección
    if i > len(A) or 0 > i:
        return sumaDeFilas(A)
    
    # Sino, se suman los elementos de la fila y se regresa ese valor
    for j in range(len(A[k])):
        acumulado += A[i-1][j]
    return acumulado
        
if __name__ == "__main__": # Función main para iniciar el código 
    # Se declara e incializa la matriz
    A : list = [[-1,-5,2],[3,-4,0],[7,6,-9]]

    # Se llama a la función para sumar la fila deseada y se imprime el resultado
    sumaFila = sumaDeFilas(A)
    print("La suma de los elementos de la fila da como resultado:")
    print(sumaFila)