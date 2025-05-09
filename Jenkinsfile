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
                bat '''
                docker rm -f frontend || echo "No frontend container"
                docker rm -f backend || echo "No backend container"
                '''
            }
        }

        stage('Build and Deploy') {
            steps {
                dir("${WORKSPACE}") {
                    bat 'docker-compose -f docker-compose.yml up --build -d'
                }
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
