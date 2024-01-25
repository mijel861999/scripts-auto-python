:: Abrir backend del proyecto de ecommerce
@echo off

start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Laragon\Laragon.lnk"
start "" "C:\Users\Usuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Postman\Postman.lnk"


:: Ruta del directorio
set "directorio=C:\Users\Usuario\workspace\php\login-app"

:: Abrir la terminal de Windows 11 en el directorio especificado
start wt -d "%directorio%"


