pipeline {
    agent {
        label 'macos-latest'
    }

    stages {
        stage('Checkout code') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    def pythonVersion = '3.x' // Choose the Python version you need
                    tool 'Python' + pythonVersion
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh 'python -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    sh 'pytest test.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Tests passed! Add post-build success actions here.'
        }
        failure {
            echo 'Tests failed! Take corrective actions.'
            // Add post-build failure actions here
        }
    }
}
