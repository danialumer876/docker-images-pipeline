pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Build and Push Images') {
            steps {
                script {
                    def images = [
                        'danialumer876/frontend:latest',
                        'danialumer876/backend:latest'
                    ]
                    for (int i = 0; i < images.size(); i++) {
                        def image = images[i]
                        dir("image-${i+1}") {
                            sh "sudo docker build -t $image ."
                            sh 'sudo echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            sh "sudo docker push $image"
                        }
                    }
                }
            }
        }
    }
    post {
      always {
        sh 'sudo docker logout'
      }
    }
}
