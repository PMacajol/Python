'''Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''

# Open the file in write mode
archivo = open('mi_archivo.txt', 'a')
archivo.write('Nuevo inicio de sesión')
archivo.close()

# Open the file in read mode
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())
archivo.close()
