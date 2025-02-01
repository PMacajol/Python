nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']
#los zip siempre tomara el tamaño de la lista mas pequeña

combinados = list(zip(nombres,edades,ciudades))

#print (combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en  {ciudad}")
    