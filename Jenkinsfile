pipeline {
  environment {
    PROJECT_NAME = 'phrasegen'
  }
  agent any
  stages {
    stage('Environment') {
      steps {
        sh '''#!/bin/bash -ex
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
            recordIssues tool: pyLint(pattern: 'tmp/pylint.log'), sourceCodeEncoding: 'UTF-8'
          }
        }
        stage('Flake8') {
          steps {
            sh '''#!/bin/bash -ex
              source venv/bin/activate
              flake8 *.py $PROJECT_NAME/**.py tests/**.py > tmp/flake8.log || true
            '''
            recordIssues tool: flake8(pattern: 'tmp/flake8.log'), sourceCodeEncoding: 'UTF-8'
          }
        }
        stage('MyPy') {
          steps {
            sh '''#!/bin/bash -ex
              source venv/bin/activate
              mypy *.py $PROJECT_NAME/**.py tests/**.py > tmp/mypy.log || true
            '''
            recordIssues tool: myPy(pattern: 'tmp/mypy.log'), sourceCodeEncoding: 'UTF-8'
          }
        }

      }
    }
    stage('Test') {
      steps {
        sh '''#!/bin/bash -ex
          source venv/bin/activate
          coverage run --source=phrasegen -m pytest -v --junitxml=tmp/unittests.xml
          coverage xml -o tmp/coverage.xml
          coverage html -d tmp/coverage
        '''
        archiveArtifacts 'tmp/unittests.xml'
        junit testResults: 'tmp/unittests.xml'
        archiveArtifacts 'tmp/coverage.xml'
        cobertura coberturaReportFile: 'tmp/coverage.xml'
        publishHTML ([
          reportName: 'HTML Coverage',
          reportDir: 'tmp/coverage',
          reportFiles: 'index.html',
          keepAll: false,
          alwaysLinkToLastBuild: false,
          allowMissing: false
        ])
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
