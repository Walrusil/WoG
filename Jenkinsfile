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
        stage('Prepare Test') {
            steps {
                script {
                    bat 'echo 1 > Scores.txt' // Prepare a valid score (between 1 and 1000)
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        def scoreUrl = "http://localhost:8777/score" // The docker is exposed on port 8777
                        bat "python tests/e2e.py ${scoreUrl}"
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