'''Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.'''

def doble_cero (*args):
    
    contador = 0
    

    for num in args:

        if contador + 1 == len(args):
            return False
    
        elif args[contador] == 0 and args [contador + 1] == 0:
            return True
        else:
            contador += 1
    return False        


print(doble_cero(1,2,3,4,5,6,6,6,7,7,8,8,9,9,9,0,0))