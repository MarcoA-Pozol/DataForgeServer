pipeline {
    agent any // This is by default, Jenkins agents can be build in Jenkins admin panel.

    environment {
        VENV_DIR = "venv"
        DOCKER_IMAGE_DB = "dataforge-db"
        DOCKER_IMAGE_APP = "dataforge-app"
        DOCKER_REGISTRY = "my-docker-registry" // Check how to generate or get this(is neccesary for pushing docker images)
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/MarcoA-Pozol/DataForge.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                sh 'python3 -m venv ${VENV_DIR}' // Create virtual environment
                sh """
                    . ${VENV_DIR}/bin/activate && \
                    pip install --upgrade pip && \ 
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate && \
                    python manage.py test
                """
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['your-server-ssh-key']) {
                    sh 'ssh user@yourserver "cd D:/Desktop/Marco/Coding/Projects/DataForge && git pull && systemctl restart gunicorn"'
                }
            }
        }
		stage('Build & Deploy PostgresDB Docker Image') {
			steps {
				sh 'docker build -t dataforge-db .'
				sh 'docker-run -d -p 8001:8001 dataforge-db'
			}
		}
		stage('Build & Deploy Docker Image') {
			steps {
				sh 'docker build -t dataforge-app .'
				sh 'docker run -d -p 8002:8002 dataforge-app'
			}
		}
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
