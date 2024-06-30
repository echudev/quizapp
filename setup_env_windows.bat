@echo off

:: Crear el entorno virtual
python -m venv env

:: Activar el entorno virtual
call env\Scripts\activate

:: Instalar las dependencias
pip install -r requirements.txt

echo "El entorno virtual se ha configurado y las dependencias se han instalado."
pause