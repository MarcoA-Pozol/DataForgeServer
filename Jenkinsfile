pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage("Clone Repository") {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MarcoA-Pozol/DataForge.git']])
            }
        }

        stage("Set Up Environment") {
            steps {
                bat "python -m venv ${VENV_DIR}"  // Use "python" instead of "python3" on Windows
                bat "call ${VENV_DIR}\\Scripts\\activate"
                bat "pip install --upgrade pip"
                bat "pip install -r requirements.txt" 
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}