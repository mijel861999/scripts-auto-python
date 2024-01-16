import shutil
import os
from datetime import datetime
import zipfile

destino = "D:\\copias-seguridad"
origenes = {
    "imagenes": "D:\\Miguel\\imagenes",
    "documentos": "D:\\Miguel\\documentos"
}

def realizar_copia_seguridad(origen, destino):
    try:
        print("Realizando copia de seguridad...")

        # Copiar todo el árbol de directorios desde el origen al destino
        shutil.copytree(origen, os.path.join(ruta_destino, os.path.basename(origen)))

        print("Copia de seguridad exitosa.")
    except Exception as e: 
        print(f"Error al realizar la copia de seguridad: {e}")

def comprimir_carpeta(carpeta, nombre_comprimido):
    destino1 = "D:\\copias-seguridad\\"
    os.chdir(destino1)

    # Comprimir la carpeta completa, incluyendo su contenido
    with zipfile.ZipFile(nombre_comprimido, "w", zipfile.ZIP_DEFLATED) as fzip:
        for root, dirs, files in os.walk(carpeta):
            for file in files:
                ruta_archivo = os.path.join(root, file)
                rel_path = os.path.relpath(ruta_archivo, carpeta)
                fzip.write(ruta_archivo, rel_path)
    shutil.rmtree(carpeta_destino)

def limpiar_directorio(destino, antiguedad_maxima_dias):
    fecha_actual = datetime.now()
    for archivo in os.listdir(destino):
        if archivo.endswith('.zip'):
            fecha_archivo = datetime.strptime(archivo.split('.')[0], "%y-%m-%d")
            diferencia_dias = (fecha_actual - fecha_archivo).days
            if diferencia_dias > antiguedad_maxima_dias:
                ruta_archivo = os.path.join(destino, archivo)
                os.remove(ruta_archivo)
                print(f"Archivo {archivo} eliminado por antigüedad.")

if __name__ == "__main__" :
    carpeta_destino = datetime.now().strftime("%y-%m-%d")
    ruta_destino = os.path.join(destino, carpeta_destino)
    nombre_comprimido = f"{carpeta_destino}.zip"
    # Crear la carpeta de destino sin verificar si existe
    os.makedirs(ruta_destino)

    for nombre_origen, ruta_origen in origenes.items():
        realizar_copia_seguridad(ruta_origen, destino)

    comprimir_carpeta(carpeta_destino, nombre_comprimido)

    # Limpiar directorio eliminando carpetas más antiguas de dos días
    antiguedad_maxima_dias = 2
    limpiar_directorio(destino, antiguedad_maxima_dias)

