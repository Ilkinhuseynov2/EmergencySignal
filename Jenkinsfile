pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker --version '
                // script {
                //     app = docker.build('fast-api:latest')
                // }
            }
        }
        

    }
}