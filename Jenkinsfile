pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }

    stage('Build') {
            steps {
                script {
                    app = docker.build('fast-api:latest')
                }
            }
        }
        

    }
