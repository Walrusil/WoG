pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Walrusil/WoG.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    bat 'docker-compose build --no-cache'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    bat 'docker-compose up -d'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        bat 'python tests/e2e.py'
                    } catch (Exception err) {
                        error "Tests failed: ${err}"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                    bat 'docker push liransilver/wog:latest'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}