pipeline {
    agent {
        label 'docker'
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                script {
                    app = docker.build('backend', '-f .ci/Dockerfile .')
                }
            }
        }
        

    }
}