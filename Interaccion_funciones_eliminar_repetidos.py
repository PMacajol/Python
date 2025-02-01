'''
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), 
y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) 
y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, 
y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
'''

def reducir_lista(lista):
    # Eliminar duplicados convirtiendo la lista a un conjunto
    lista_sin_duplicados = list(set(lista))
    
    # Eliminar el valor más alto
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    
    return lista_sin_duplicados

def promedio(lista):
    return sum(lista) / len(lista)

# Crear la variable lista_numeros
lista_numeros = [1, 2, 15, 7, 2]

# Reducir la lista
lista_reducida = reducir_lista(lista_numeros)

# Calcular el promedio de la lista reducida
resultado_promedio = promedio(lista_reducida)

print(lista_reducida)  
print(resultado_promedio)  
