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

        stage('Clean Old Containers and Images') {
            steps {
                bat '''
                docker stop frontend || exit 0
                docker rm frontend || exit 0
                docker stop backend || exit 0
                docker rm backend || exit 0

                docker rmi -f fullstack-frontend || exit 0
                docker rmi -f fullstack-backend || exit 0
                '''
            }
        }

        stage('Build Backend Image') {
            steps {
                bat 'docker build --no-cache -t fullstack-backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                bat 'docker build --no-cache -t fullstack-frontend ./frontend'
            }
        }

        stage('Run Final Containers') {
            steps {
                bat '''
                docker run -d -p 9000:9000 --name backend fullstack-backend
                docker run -d -p 9090:80 --name frontend fullstack-frontend
                '''
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
