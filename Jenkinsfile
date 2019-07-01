pipeline {
    environment {
      PROJECT_NAME = 'case_study_2'
      ENV_NAME = 'test'
    }
    agent any
    stages {
        stage('1 Set up venv') {
            sh '''
            python3 -m venv ~/cs2/cs2_venv'
            source ~/venvs/$PROJECT_NAME/$ENV_NAME/bin/activate
            '''
        stage('2 Validate style and quality') {
            parallel {
                stage('2.1 PyLint') {
                    steps {
                        sh '''#!/bin/bash -ex
                        pylint --rcfile=.pylintrc --output-format=parseable *.py $PROJECT_NAME/**.py > pylint.log || true
                        '''
                        warnings(parserConfigurations: [[parserName: 'PyLint', pattern: 'pylint.log']])
                        archiveArtifacts(artifacts: 'pylint.log', fingerprint: true)
                    }
                }
                stage('2.2 Flake8') {
                    steps {
                        sh '''#!/bin/bash -ex
                        flake8 *.py $PROJECT_NAME/ > flake8.log || true
                        '''
                        warnings(parserConfigurations: [[parserName: 'Pep8', pattern: 'flake8.log']])
                        archiveArtifacts(artifacts: 'flake8.log', fingerprint: true)
                    }
                }
            }
        }
        stage('3 Run tests') {
            steps {
                sh '''#!/bin/bash -ex
                coverage run -m pytest -v --junitxml=tmp/unittests.xml
                coverage xml -o tmp/coverage.xml
                '''
            }
        }
    }
}
