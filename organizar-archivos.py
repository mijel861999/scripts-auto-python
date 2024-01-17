import shutil
import os

carpeta_descarga = 'C:\\Users\\Usuario\\Downloads\\'

destinos = {
    "imagenes": "D:\\Miguel\\imagenes\\",
    "archivos_ibit": "D:\\Miguel\\archivos_ibit\\",
    "archivos": ""
}


if __name__ == '__main__':
    print("Ejecutando archivo para organizar archivos...")

    for archivo in os.listdir(carpeta_descarga):
        name, extension = os.path.splitext(carpeta_descarga + archivo)

        if '_ibit' in archivo:
            shutil.move(carpeta_descarga + archivo, destinos["archivos_ibit"] + archivo)
            print("------Archivos Ibit----------------------")
            print(carpeta_descarga + archivo)
            print(destinos["archivos_ibit"] + archivo)
            print("-----------------------------------------")

        if extension in [".jpg", ".jpeg", ".png"]:
            shutil.move(carpeta_descarga + archivo, destinos["imagenes"] + archivo)
            print("------Imagenes----------------------")
            print(carpeta_descarga + archivo)
            print(destinos["archivos_ibit"] + archivo)
            print("-----------------------------------------")
