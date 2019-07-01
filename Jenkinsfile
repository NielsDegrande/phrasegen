pipeline {
    environment {
      PROJECT_NAME = 'phrasegen'
    }
    agent any
    stages {
        stage('1 Set up virtual environment') {
            steps {
                sh '''#!/bin/bash -ex
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt -q
                '''
            }
        }
        stage('2 Validate style and quality') {
            parallel {
                stage('2.1 PyLint') {
                    steps {
                        sh '''#!/bin/bash -ex
                            source venv/bin/activate -q
                            pylint --rcfile=.pylintrc --output-format=parseable *.py $PROJECT_NAME/**.py tests/**.py > tmp/pylint.log || true
                        '''
                    }
                }
                stage('2.2 Flake8') {
                    steps {
                        sh '''#!/bin/bash -ex
                            source venv/bin/activate
                            flake8 *.py $PROJECT_NAME/**.py tests/**.py > tmp/flake8.log || true
                        '''
                    }
                }
                stage('2.3 MyPy') {
                    steps {
                        sh '''#!/bin/bash -ex
                            source venv/bin/activate
                            mypy *.py $PROJECT_NAME/**.py tests/**.py > tmp/mypy.log || true
                        '''
                    }
                }

            }
        }
        stage('3 Run tests') {
            steps {
                sh '''#!/bin/bash -ex
                    source venv/bin/activate
                    coverage run --source=phrasegen -m pytest -v --junitxml=tmp/unittests.xml
                    coverage xml -o tmp/coverage.xml
                    coverage html -d tmp/html_coverage
                '''
                archiveArtifacts 'tmp/unittests.xml'
                junit testResults: 'tmp/unittests.xml'
                archiveArtifacts 'tmp/coverage.xml'
                cobertura coberturaReportFile: 'tmp/coverage.xml'
                publishHTML ([
                    allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: false,
                    reportDir: 'tmp/html_coverage',
                    reportFiles: 'index.html',
                    reportName: 'HTML Coverage Report'
                ])
            }
        }
        stage('4 Deployment') {
            parallel {
                stage('4.1 Deploy in staging') {
                    when {
                        branch 'staging'
                    }
                    steps {
                        sh 'echo "Build production image and upload to registry"'
                    }
                }
                stage('4.2 Deploy in production') {
                    when {
                        branch 'master'
                    }
                    steps {
                        sh 'echo "Build production image and upload to registry"'
                    }
                }
            }
        }
    }
}
