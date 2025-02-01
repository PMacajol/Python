'''buscar archivos en una ruta especifica'''
''' os.chdir = movilizarse entre las carpetas o directorios
    os.makedirs = creacion de carpeta nueva y solo se pasa el parametro en donde querramos que se cree'''

import os
ruta = os.chdir('C:\\Users\\62181\\Desktop\\Pruebas')

archivo = open('test.txt')

print(archivo.read())