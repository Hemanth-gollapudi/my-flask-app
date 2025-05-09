pipeline {
    agent any

    triggers {
        pollSCM('* * * * *') 
    }

    environment {
        REPO_URL = 'https://github.com/Hemanth-gollapudi/my-flask-app.git' 
        BRANCH_NAME = 'main' 
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage('Clean Old Containers') {
            steps {
                sh 'docker rm -f frontend backend || true'
            }
        }

        stage('Build and Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Something went wrong!'
        }
    }
}
