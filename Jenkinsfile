pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/brun0be/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t docker1906/wog-app .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p8777:8777 docker1906/wog-app'
            }
        }
        stage('E2E Test') {
            steps {
                sh 'pip3 install selenium'
                sh 'python3 ./tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker login'
                sh 'docker tag docker1906/wog-app docker1906/wog-app:latest'
                sh 'docker push docker1906/wog-app:latest'
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Clean Completed'
            }
        }
    }
}