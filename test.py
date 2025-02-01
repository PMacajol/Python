

def primos (lista_numeros):
    lista_pri = []
    sum_pri = 0 
    for n in lista_numeros:
        if n % 2 == 0:
            pass
        else:
            lista_pri.append(n)
            sum_pri += n
    return lista_pri,sum_pri

lista = [1,2,3,4,5,6,7]
result = primos(lista)
print (result)
