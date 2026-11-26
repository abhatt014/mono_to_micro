pipeline {
  agent {label 'testing'}       // where the build runs

  environment {
    IMAGE = 'amitfreeze/aug_wd_mono'
    TAG   = "${env.BUILD_NUMBER}"
    APP = "school-app"
  }

  stages {

    stage('build') {
      steps {
        sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
      }
    }
   stage('push') {
       steps {
           withCredentials([usernamePassword(credentialsId: 'docker_hub_cred', passwordVariable: 'HUBPASS', usernameVariable: 'HUBUSER')]) {
                 sh ' echo "$HUBPASS" | docker login -u $HUBUSER --password-stdin ; '  
                 sh 'docker push $IMAGE:$BUILD_NUMBER'
                 sh 'docker push $IMAGE:latest'
                 sh 'docker rm $APP -f || true'
                 
            }       
         
       }
   } 
  stage('deploy') {
      steps {
            sh 'docker run -d --name $APP --network school-net -p 5000:5000 $IMAGE:latest'
      }
  } 
  }


}

