:: Abrir una terminal con todas mis notas
@echo off

:: Ruta del directorio
set "directorio=C:\Users\Usuario\notes"

:: Abrir la terminal de Windows 11 en el directorio especificado
start wt -d "%directorio%"
