def validar_3_cifras(lista):
    for n in lista:
        if n in range (100,1000):
            return True
    else:
        pass
    return False

resultado = validar_3_cifras([55,99,101])
print(resultado)