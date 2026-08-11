pipeline{
    agent any
    environment {
        APP_ENV='test'
    }
        stages{

            // stage('PATH debug'){
            //     steps{
            //         bat '''
            //         echo ==========================
            //         echo PATH
            //         echo ==========================
            //         echo %PATH%

            //         echo ==========================
            //         echo Python location
            //         echo ==========================
            //         where python


            //         '''
            //     }
            // }

            stage('Application environment'){
                steps{
                    bat 'echo Application Environment= %APP_ENV%'
                }
            }
            stage('environment'){
                steps{
                    bat '''
                    python --version
                    pip --version

                    '''
                }
            }
            // stage('workspace debug'){
            //     steps{
            //         bat '''
            //         echo Current Directory:
            //         cd

            //         echo Jenkins Workspace:
            //         echo %WORKSPACE%

            //         echo Files available:
            //         dir
            //         '''
            //     }
            // }
            stage('install dependencies'){
                steps{
                    bat 'pip install -r requirements.txt'
                }
            }
            stage('unit tests'){
                environment{
                        TEST_TYPE='smoke'
                    }
                steps{
                    bat '''
                    echo Test type = %TEST_TYPE
                    pytest -v
                    '''

                    

                }
            }
        }
    }
