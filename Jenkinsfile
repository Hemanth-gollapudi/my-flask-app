pipeline {
    agent any

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
                script {
                    sh 'docker rm -f frontend || echo "No frontend container"'
                    sh 'docker rm -f backend || echo "No backend container"'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker build -t hemanthkumar21/my-flask-frontend:latest ./frontend'
                    sh 'docker build -t hemanthkumar21/my-flask-backend:latest ./backend'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                }
            }
        }

        stage('Push Images to DockerHub') {
            steps {
                script {
                    sh 'docker push hemanthkumar21/my-flask-frontend:latest'
                    sh 'docker push hemanthkumar21/my-flask-backend:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    script {
                        // Apply YAMLs with kubeconfig path
                        sh 'KUBECONFIG=${KUBECONFIG_FILE} kubectl apply -f k8s/'
                        // Wait for rollout
                        sh 'KUBECONFIG=${KUBECONFIG_FILE} kubectl rollout status deployment/backend-deployment'
                        sh 'KUBECONFIG=${KUBECONFIG_FILE} kubectl rollout status deployment/frontend-deployment'
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build, Docker push, and Kubernetes deployment completed!'
        }
        failure {
            echo '❌ Deployment failed.'
        }
    }
}
