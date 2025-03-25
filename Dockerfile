# Usar una imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Ejecutar la aplicación al iniciar el contenedor
CMD ["python", "calculator.py"]
