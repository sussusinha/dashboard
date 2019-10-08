pipeline {
    agent any;
    stages {
        stage('Preparação') {
            steps {
                echo "Preparando ...";
                sleep 10;
            }
        }
        stage('Buildando') {
            steps {
                echo "Buildando ...";
                sleep 10;
            }
        }
        stage('Resultado') {
            steps {
                echo "Sucesso !";
            }
        }
    }
}