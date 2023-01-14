pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Checkout Git Repo') {
            steps {
            checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/danialumer876/docker-images-pipeline.git']])
            }
        }
        stage('Build and Push frontend Image') {
            steps {
                script {
                        def image1 = 'danialumer876/frontend:latest'
                        dir("image-1") {
                            sh "sudo docker build -t $image1 ."
                            sh 'sudo echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            sh "sudo docker push $image1"
                            sh 'sudo docker logout'
                        }
                    
                }
            }
            
        }
        stage('Build and Push backend Image') {
            steps {
                script {
                        def image2 = 'danialumer876/backend:latest'
                        dir("image-2") {
                            sh "sudo docker build -t $image2 ."
                            sh 'sudo echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            sh "sudo docker push $image2"
                            sh 'sudo docker logout'
                        }
                    
                }
            }
            
        }
        stage('Deploying App to Kubernetes') {
            steps {
                script {
                         checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/danialumer876/docker-images-pipeline.git']])
                          kubernetesDeploy(configs: "completeproject.yml", kubeconfigId: "mykubeconfig")
                }
            }
        }
    }
}

