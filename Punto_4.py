def sumaDeColumnas(A: list)-> int: # Al ingresar la matriz devuelve el valor entero de la suma de los elementos de una columna 
    # Se declaran e inicializan las variables locales
    j = int(input("¿Qué número de columna deseas sumar?"))
    i : int = 0
    acumulado: int = 0

    # Si la columna elegida es mayor a las existentes, o se ingresa un valor negativo, se vuelve a la elección
    if j > len(A[i]) or 0 > j :
        return sumaDeColumnas(A)
    
    # Sino, se suman los elementos de la columna y se regresa ese valor
    for i in range(len(A)):
        acumulado += A[i][j-1]
    return acumulado
        
if __name__ == "__main__": # Función main para iniciar el código 
    # Se declara e incializa la matriz
    A : list = [[3,-4,0],[7,6,-9],[-1,-5,2]]

    # Se llama a la función para sumar la columna deseada y se imprime el resultado
    sumaColumna = sumaDeColumnas(A)
    print("La suma de los elementos de la columna da como resultado:")
    print(sumaColumna)