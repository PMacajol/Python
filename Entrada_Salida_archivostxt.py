mi_archivo = open('prueba.txt')



print(mi_archivo.read())


mi_archivo.close()

'''Abre el archivo texto.txt e imprime únicamente la segunda línea.'''

mi_archivo = open('texto.txt')

mi_archivo.readline()

print(mi_archivo.readline())


mi_archivo.close()