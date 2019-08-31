pipeline {
  environment {
    PROJECT_NAME = 'phrasegen'
  }
  agent any
  stages {
    stage('Inspect') {
      steps {
        sh '''#!/bin/bash -ex
          rm -rf .tox || true
          pip install tox
          tox -e jenkins
        '''
      }
      post {
        always {
          recordIssues tool: pyLint(pattern: 'tmp/pylint.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
          archiveArtifacts 'tmp/pylint.log'

          recordIssues tool: flake8(pattern: 'tmp/flake8.log'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
          archiveArtifacts 'tmp/flake8.log'

          recordIssues tool: myPy(pattern: 'tmp/mypy.xml'), sourceCodeEncoding: 'UTF-8', qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
          archiveArtifacts 'tmp/mypy.xml'

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
              source .tox/jenkins/bin/activate
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
              source .tox/jenkins/bin/activate
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
              source .tox/jenkins/bin/activate
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
              source .tox/jenkins/bin/activate
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
        message: "SUCCESSFUL: Job ${env.JOB_NAME} [${env.BUILD_NUMBER}] (${env.BUILD_URL})",
        teamDomain: '',
        channel: '',
        tokenCredentialId: ''
      )
    }
    failure {
      /* Post status to Slack. */
      slackSend (
        color: '#FF0000',
        message: "FAILED: Job ${env.JOB_NAME} [${env.BUILD_NUMBER}] (${env.BUILD_URL})",
        teamDomain: '',
        channel: '',
        tokenCredentialId: ''
      )
    }
  }
}
