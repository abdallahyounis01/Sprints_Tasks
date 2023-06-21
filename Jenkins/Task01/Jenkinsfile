pipeline {
     agent any
   
    stages {
        stage('Check') {
            steps {
                echo "Checking Your Code"
               
            }
        }

        stage('Test') {
            when {
                expression{
                    params.Bool-Param == true 
                }
            }
            steps {
                echo "Testing Your App" 
            }
        }
        
        stage('Deployment') {  
            steps {
                echo "Your Code Is Deploying"
                echo "This Build Number $BUILD_NUMBER"
            }
        }    
    }

}
