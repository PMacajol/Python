'''Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre,
y a continuación, una cantidad indefinida de números.
La función debe devolver el siguiente mensaje:
"{nombre}, la suma de tus números es {suma_numeros}"'''


def numeros_persona(nombre, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"


resultado = numeros_persona("Federico", 75, 20, 65)

print(resultado)
