# Quizapp

## Configuración del Entorno Virtual e Instalación de Dependencias

Este proyecto utiliza un entorno virtual para manejar las dependencias.
Seguí las instrucciones a continuación para configurarlo y activarlo en Windows y Linux.

## Requisitos Previos

- Python instalado en tu sistema.
- Archivo `requirements.txt` con las dependencias listadas.

## Instrucciones para Windows

1. Abrí el símbolo del sistema (Command Prompt).
2. Navegá al directorio del proyecto donde se encuentra `setup_env_windows.bat` y `requirements.txt`.
3. Ejecutá el siguiente comando:

    ```sh
    setup_env_windows.bat
    ```

## Instrucciones para Linux

1. Abrí una terminal.
2. Navegá al directorio del proyecto donde se encuentra el `Makefile` y `requirements.txt`.
3. Ejecutá el siguiente comando para crear y configurar el entorno virtual e instalar las dependencias:

    ```sh
    make
    ```
