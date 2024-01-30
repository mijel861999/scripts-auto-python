:: IBIT - Abrir proyecto PCR
@echo off

:: Ruta del directorio
set "directorio=C:\Users\Usuario\workspace\ibit\PCR\MiPCR-Front"
set "ruta_one_note=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk"

:: Abrir terminal
start wt -d "%directorio%"

:: Abrir OneNote
start "" "%ruta_one_note%"

