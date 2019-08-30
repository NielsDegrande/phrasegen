pipeline {
  environment {
    PROJECT_NAME = 'phrasegen'
  }
  agent any
  stages {
    stage('Venv') {
      steps {
        sh '''#!/bin/bash -ex
        rm -rf .venv || true
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        pip install -r requirements_dev.txt
        mkdir -p tmp
        '''
      }
    }
    stage('Style') {
      parallel {
        stage('PyLint') {
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate -q
              pylint --rcfile=.pylintrc --output-format=parseable *.py $PROJECT_NAME/**.py tests/**.py > tmp/pylint.log || true
            '''
          }
          post{
            always {
              recordIssues tool: pyLint(pattern: 'tmp/pylint.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
              archiveArtifacts 'tmp/pylint.log'
            }
          }
        }
        stage('Flake8') {
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate
              flake8 *.py $PROJECT_NAME/**.py tests/**.py > tmp/flake8.log || true
            '''
          }
          post {
            always {
              recordIssues tool: flake8(pattern: 'tmp/flake8.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
              archiveArtifacts 'tmp/flake8.log'
            }
          }
        }
        stage('MyPy') {
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate
              mypy *.py $PROJECT_NAME/**.py tests/**.py > tmp/mypy.log || true
            '''
          }
          post {
            always {
              recordIssues tool: myPy(pattern: 'tmp/mypy.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
              archiveArtifacts 'tmp/mypy.log'
            }
          }
        }

      }
    }
    stage('Test') {
      steps {
        sh '''#!/bin/bash -ex
          source .venv/bin/activate
          coverage run --source=phrasegen -m pytest -v --junitxml=tmp/unittests.xml
          coverage xml -o tmp/coverage.xml
          coverage html -d tmp/coverage
        '''
      }
      post {
        always {
          archiveArtifacts 'tmp/unittests.xml'
          junit 'tmp/unittests.xml'
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
    }
    stage('Deploy') {
      parallel {
        stage('Feature') {
          when {
            not {
              anyOf {
                branch 'master';
                branch 'staging';
                expression { BRANCH_NAME ==~ /^PR-\d+$/ }
              }
            }
          }
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate
              echo "Do non-master-nor-staging stuff"
            '''
          }
        }
        stage('PR') {
          when {
            expression { BRANCH_NAME ==~ /^PR-\d+$/ }
          }
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate
              echo "Do PR stuff"
            '''
          }
        }
        stage('Staging') {
          when {
            branch 'staging'
          }
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate
              echo "Build staging image and upload to registry"
            '''
          }
        }
        stage('Production') {
          when {
            branch 'master'
          }
          steps {
            sh '''#!/bin/bash -ex
              source .venv/bin/activate
              echo "Build production image and upload to registry"
              ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ansible/production ansible/site.yml
            '''
          }
        }
      }
    }
  }
  post {
    always {
      /* Clean up workspace. */
      deleteDir()
      /* Clean up tmp directory. */
      dir("${workspace}@tmp") {
          deleteDir()
      }
    }
    success {
      /* Post status to Slack. */
      slackSend (
        color: '#00FF00',
        message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})",
        teamDomain: '',
        channel: '',
        tokenCredentialId: ''
      )
    }
    failure {
      /* Post status to Slack. */
      slackSend (
        color: '#FF0000',
        message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})",
        teamDomain: '',
        channel: '',
        tokenCredentialId: ''
      )
    }
  }
}
