'''Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''

# Open the file in write mode
archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo.close()

# Open the file in read mode
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())
archivo.close()
