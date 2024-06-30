# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
& .\env\Scripts\Activate.ps1

# Instalar las dependencias
pip install -r requirements.txt

Write-Host "El entorno virtual se configuró y las dependencias se instalaron."