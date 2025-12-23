#Imagen base de Python ligera
FROM python:3.9-slim

#Directorio de trabajo dentro del contenedor
WORKDIR /app

#Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copiar el código de la app
COPY app.py .

#Exponer el puerto donde corre Flask
EXPOSE 5000

#Comando para ejecutar la app
CMD ["python", "app.py"]
