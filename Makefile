# Makefile para configurar el entorno virtual y instalar dependencias

.PHONY: all setup activate clean

# Comando por defecto
all: setup

# Crear y configurar el entorno virtual
setup:
	python3 -m venv env
	@echo "Entorno virtual creado."
	. env/bin/activate && pip install -r requirements.txt
	@echo "Dependencias instaladas."

# Activar el entorno virtual
activate:
	@echo "Para activar el entorno virtual, ejecutá:"
	@echo "source env/bin/activate"

# Limpiar el entorno virtual
clean:
	rm -rf venv
	@echo "Entorno virtual eliminado."
