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
                echo "hello world"
                // script {
                //     app = docker.build('fast-api', '-f .ci/Dockerfile .')
                // }
                
            }
        }
        

    }
}