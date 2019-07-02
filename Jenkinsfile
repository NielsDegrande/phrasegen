pipeline {
  environment {
    PROJECT_NAME = 'phrasegen'
  }
  agent any
  stages {
    stage('Venv') {
      steps {
        sh '''#!/bin/bash -ex
        rm -r venv
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt -q
        '''
      }
    }
    stage('Style') {
      parallel {
        stage('PyLint') {
          steps {
            sh '''#!/bin/bash -ex
              source venv/bin/activate -q
              pylint --rcfile=.pylintrc --output-format=parseable *.py $PROJECT_NAME/**.py tests/**.py > tmp/pylint.log || true
            '''
            recordIssues tool: pyLint(pattern: 'tmp/pylint.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
            archiveArtifacts 'tmp/pylint.log'
          }
        }
        stage('Flake8') {
          steps {
            sh '''#!/bin/bash -ex
              source venv/bin/activate
              flake8 *.py $PROJECT_NAME/**.py tests/**.py > tmp/flake8.log || true
            '''
            recordIssues tool: flake8(pattern: 'tmp/flake8.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
            archiveArtifacts 'tmp/flake8.log'
          }
        }
        stage('MyPy') {
          steps {
            sh '''#!/bin/bash -ex
              source venv/bin/activate
              mypy *.py $PROJECT_NAME/**.py tests/**.py > tmp/mypy.log || true
            '''
            recordIssues tool: myPy(pattern: 'tmp/mypy.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
            archiveArtifacts 'tmp/mypy.log'
          }
        }

      }
    }
    stage('Test') {
      steps {
        sh '''#!/bin/bash -ex
          source venv/bin/activate
          coverage run --source=phrasegen -m pytest -v --junitxml=unittests.xml
          coverage xml -o tmp/coverage.xml
          coverage html -d tmp/coverage
        '''
        archiveArtifacts 'unittests.xml'
        junit testResults: 'unittests.xml'
        archiveArtifacts 'tmp/coverage.xml'
        cobertura coberturaReportFile: 'tmp/coverage.xml'
        publishHTML target: [
          allowMissing: false,
          alwaysLinkToLastBuild: false,
          keepAll: false,
          reportDir: 'tmp/coverage',
          reportFiles: 'index.html',
          reportName: 'HTML Coverage'
        ]
      }
    }
    stage('Deploy') {
      parallel {
        stage('Staging') {
          when {
            branch 'staging'
          }
          steps {
            sh 'echo "Build production image and upload to registry"'
          }
        }
        stage('Production') {
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
