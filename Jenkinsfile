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
                    // Clean old containers if any exist
                    sh 'docker rm -f frontend || echo "No frontend container"'
                    sh 'docker rm -f backend || echo "No backend container"'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Build frontend and backend Docker images
                    sh 'docker build -t hemanthkumar21/my-flask-frontend:latest ./frontend'
                    sh 'docker build -t hemanthkumar21/my-flask-backend:latest ./backend'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        // Log in to DockerHub
                        sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                    }
                }
            }
        }

        stage('Push Images to DockerHub') {
            steps {
                script {
                    // Tag and push images to DockerHub
                    sh 'docker push hemanthkumar21/my-flask-frontend:latest'
                    sh 'docker push hemanthkumar21/my-flask-backend:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    script {
                        // Set the Kubernetes config
                        sh 'export KUBECONFIG=${KUBECONFIG_FILE}'
                        // Apply Kubernetes configurations
                        sh 'kubectl apply -f k8s/'
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
