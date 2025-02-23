#!/bin/bash

# Variables - Reemplaza con tu usuario y repositorio
github_user="ALEXPAD05"
github_repo="activation_functions_padilla"
repo_url="https://github.com/$github_user/$github_repo.git"

# Clonar el repositorio
echo "Clonando el repositorio desde $repo_url..."
git clone $repo_url

# Entrar en la carpeta del proyecto
cd $github_repo || { echo "Error: No se pudo acceder al directorio $github_repo"; exit 1; }

# Verificar si hay un package.json para instalar dependencias Node.js
if [ -f "package.json" ]; then
    echo "Instalando dependencias con npm..."
    npm install
fi

# Verificar si hay un requirements.txt para instalar dependencias Python
if [ -f "requirements.txt" ]; then
    echo "Creando entorno virtual e instalando dependencias Python..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# Ejecutar el proyecto (ajusta esto según tu proyecto)
if [ -f "main.py" ]; then
    echo "Ejecutando aplicación Python..."
    python main.py
elif [ -f "app.js" ]; then
    echo "Ejecutando aplicación Node.js..."
    npm start
elif [ -f "docker-compose.yml" ]; then
    echo "Ejecutando con Docker..."
    docker-compose up
else
    echo "No se encontró un archivo de ejecución específico. Revisa el README.md para más instrucciones."
fi
