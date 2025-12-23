pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins descarga el código de GitHub
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    // Aquí Jenkins hace el "docker build" que tú hacías a mano
                    echo "Construyendo la imagen de Docker..."
                    sh "docker build -t mi-app-python:latest ."
                }
            }
        }

        stage('Test') {
            steps {
                // Una prueba simple: preguntar a la imagen si tiene Python instalado
                echo "Verificando instalación..."
                sh "docker run --rm mi-app-python:latest python --version"
            }
        }

        stage('Cleanup') {
            steps {
                // Limpiamos contenedores huérfanos para no llenar el disco
                echo "Limpiando entorno..."
                sh "docker image prune -f"
            }
        }
    }
}
