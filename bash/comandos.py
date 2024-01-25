# Abrir todos los comandos personalizados
import os

def obtener_descripcion(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        # Lee la primera línea del archivo
        primera_linea = f.readline().strip()
    return primera_linea

def obtener_informacion_archivos(ruta_carpeta):
    informacion_archivos = {}

    # Obtén la lista de archivos en la carpeta
    archivos_en_carpeta = [archivo for archivo in os.listdir(ruta_carpeta)]

    # Itera sobre los archivos y obtén la descripción
    for archivo in archivos_en_carpeta:
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        descripcion = obtener_descripcion(ruta_completa)
        informacion_archivos[archivo] = descripcion

    return informacion_archivos

# Especifica la ruta de tu carpeta
ruta_carpeta = 'C:\\Users\\Usuario\\scripts\\bash'

# Llama a la función para obtener la información de los archivos
informacion_archivos = obtener_informacion_archivos(ruta_carpeta)

# Muestra la información en el formato deseado
for nombre_archivo, descripcion in informacion_archivos.items():
    print(f'"{nombre_archivo}" : "{descripcion}"')

