pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                script {
                    app = docker.build('fast-api')
                }
            }
        }
        

    }
}