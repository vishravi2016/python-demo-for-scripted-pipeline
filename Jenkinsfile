pipeline{
    agent any
        stages{
            stage('environment'){
                steps{
                    bat '''
                    python --version
                    pip --version

                    '''
                }
            }
            stage('install dependencies'){
                steps{
                    bat 'pip install -r requirement.txt'
                }
            }
            stage('tests'){
                steps{
                    bat 'pytest -v'

                }
            }
        }
    }
