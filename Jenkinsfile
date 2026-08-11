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
            stage('workspace debug'){
                steps{
                    bat '''
                    echo Current Directory:
                    cd

                    echo Jenkins Workspace:
                    echo %WORKSPACE%

                    echo Files available:
                    dir
                    '''
                }
            }
            stage('install dependencies'){
                steps{
                    bat 'pip install -r requirements.txt'
                }
            }
            stage('tests'){
                steps{
                    bat 'pytest -v'

                }
            }
        }
    }
