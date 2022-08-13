pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                echo 'docker --version '
                script {
                    app = docker.build('fast-api:latest')
                }
            }
        }
        

    }
}