pipeline {
    agent none
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