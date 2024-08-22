# Reto_11
***
Solución de los problemas asignados - Realizado por Lucas García Álvarez

![logo](https://i.ibb.co/440n654/A-adir-un-t-tulo.png)

*Nota*: Para esta actividad se utilizó Python 3.12.5
## Ejercicio 1
***
Se trabajó en desarrollar un programa que permita realizar la suma/resta de matrices. Para esto el programa tuvo que validar las condiciones necesarias para ejecutar la operación, es decir, que ambas matrices tuviesen la misma cantidad de filas y columnas, para así operar elementos que coincidan en sus coordenadas, lo que cuál sucede en la siguiente función:
```python
def comprobar (A:list, B:list ) -> bool: # Al recibir ambas listas las compara y verifica si son operables o no
    for i in range(len(A)): # Recorre filas
        for j in range(len(A[i])): # Recorre cada columna
            if len(A[i]) != len(B[i]): # Si no coincide alguna longitud no son operables
                return False
    return True # Si todas las longitudes coinciden es operable
```
Luego de esto, se opera facilmente al sumar o restar cada elemento de una matriz por su semejante en la otra.
```python
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
```
Finalmente, se imprimen resultados y se hace uso de las funciones en la función main.
```python
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
```
## Ejercicio 2
***
El propósito era realizar un programa que permita realizar el producto de matrices, y con ello, el programa debe validar las condiciones necesarias para ejecutar la operación, las cuales en este caso son que la cantidad de filas de la primera matriz, sean iguales a la cantidad de columnas de la segunda matriz, tal como se comprueba en esta función:
```python
def comprobar (A:list, B:list ) -> bool: # Se ingresan las dos funciones y se comprueba su capacidad de multiplicarse
    if len(A[0]) != len(B): # Si la cantidad de filas de A es distinta a la de columnas de B, no son multiplicables
        return False
    return True # En caso de que las longitudes sean congruentes, se valida la condición
```
Luego se halla el producto de las matrices al sumar el producto de elementos de columnas distintas en la misma fila de A, por elementos de filas distintas de la misma columna de B, esto entrega un solo valor para cada fila, y se va iterando para, al repetir el proceso, rellenar todas las filas y columnas.
```python
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
```
Para concluir se imprime la matriz y se ejecutan dentro de la función main todas las demás funciones
```python
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
```
## Ejercicio 3
***
Se llevó a cabo un programa capaz de hallar la matriz transpuesta de una matriz ingresada.

Para esto, la función itera entre filas seleccionando el dato en la misma columna y una vez completo estos datos forman una columna de la función transpuesta, así hasta tomar el último dato de la última fila y última columna.
```python
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
```
De ahí se crea la función para imprimir la matriz y se ejecutan ambas en la función main que da inicio al código:
```python
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
```
## Ejercicio 4
***
El objetivo fue desarrollar un programa que sume los elementos de una columna dada de una matriz.

Esto fue muy sencillo, en la función únicamente se iteró entre filas dentro de la misma columna y se sumaron los valores allí presentes y luego se ejecutó esta misma en la función main.
```python
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
```
## Ejercicio 5
***
Bastante similar al anterior, se tuvo que desarrollar un programa capaz de sumar todos los elementos dentro de una fila de la matriz.

Para esto se hizo lo contrario al ejercicio previo, en la función se iteró entre columnas en la misma fila y se sumó cada valor allí presente, para luego ejecutarse dentro de la función main.
```python
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
```
