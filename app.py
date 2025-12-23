from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Usamos una variable de entorno para demostrar configuración externa
    nombre = os.getenv('USER_NAME', 'Mundo')
    return f'<h1>Que pdo mi vic {nombre}!</h1><p>Gay el que lo lea, el creador es inmune.</p>'

if __name__ == '__main__':
    # Escuchamos en todas las interfaces (0.0.0.0) para que Docker pueda redirigir el tráfico
    app.run(host='0.0.0.0', port=5000)
