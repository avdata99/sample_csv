import csv

archivo_de_origen = 'test-final-2017.csv'
archivo_de_destino = 'test-final-2017-recortado.csv'
campos_a_quitar = ['observacion', 'beneficiario']

# abrir el archivo CSV
csvfile = open(archivo_de_origen, 'r')
# inicializar el lector del archivo incluido en la librería CSV
reader = csv.DictReader(csvfile)

# obetener los nombres de las columnas
fieldnames = reader.fieldnames

# preparar nuevo encabezado sin el campo que queremos quitar
# esta sería la forma de hacerlo (pero es más dificil de entender)
# new_fieldnames = [field for field in fieldnames if field not in campos_a_quitar]

# forma simple de tener una lista basada en otra pero sacando algunos elementos
new_fieldnames = []
for field in fieldnames:
    if field not in campos_a_quitar:
        new_fieldnames.append(field)

# preparar un archivo nuevo para grabar con los datos procesados
new_file = open(archivo_de_destino, 'w')
writer = csv.DictWriter(new_file, fieldnames=new_fieldnames)

# escribir la fila de encabezados
writer.writeheader()

# leer una a una las lineas del archivos de origen        
for row in reader:
    # row es un diccionario con cada una de las líneas del CSV
    # ejemplo row['Año'] es el año

    # copiar la fila para despues modificarla
    new_row = row.copy()

    # quitar los campos que no quiero
    for campo in campos_a_quitar:
        new_row.pop(campo)

    # ejemplo: pasar a mayúsculas el subprograma
    new_row['Sub programa'] = row['Sub programa'].upper()

    # ejemplo de transformar un campo a numero y hacer cálculos
    anio = row['Año']  # esto es un texto, no un numero listo para procesar
    anio = anio.strip()  # quitar espacios adelante o atras (muy comun en estos casos)
    anio = int(anio)  # transformar a numero entero (dará error si no es posible)
    
    anio_calculado = anio * 3
    new_row['Año'] = anio_calculado

    # separar la partida en codigo y nombre
    partes_partida = row['Partida'].split('-')  # split crea una lista de elementos a partir de un string separandolo por un caracter definido como parametro
    codigo_partida = partes_partida[0].strip()
    nombre_partida = partes_partida[1].strip()
    # usar solo el nombre
    new_row['Partida'] = nombre_partida

    # agregar esta fila corregida al nuevo archivo
    writer.writerow(new_row)

    # imprimir algo en pantalla
    print('Fila Año: {} Partida:{}'.format(anio, nombre_partida))



