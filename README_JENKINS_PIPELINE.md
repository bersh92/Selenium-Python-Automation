# Jenkins Pipeline for orangeHrm

This Jenkins pipeline is set up to automate the testing process for the orangeHrm project. It includes steps to install dependencies, check out the project code, set up the Python environment, run tests, and generate an Allure report.

## Table of Contents

- [Setting up Periodic Builds](#setting-up-periodic-builds)
  - [Cron Syntax Examples](#cron-syntax-examples)
- [Pipeline Stages Explanation](#pipeline-stages-explanation)
  - [Environment](#environment)
  - [Install Dependencies](#install-dependencies)
  - [Checkout](#checkout)
  - [Setup Python](#setup-python)
  - [Verify pytest Installation](#verify-pytest-installation)
  - [Create .env File with Jenkins Credentials](#create-env-file-with-jenkins-credentials)
  - [Run Tests](#run-tests)
  - [Generate Allure Report](#generate-allure-report)
- [Post Actions](#post-actions)
- [Complete Jenkins Pipeline Script](#complete-jenkins-pipeline-script)

## Setting up Periodic Builds

To configure periodic builds in Jenkins, follow these steps:

1. Go to your Jenkins job.
2. Click on "Configure".
3. Check the "Build periodically" option under the "Build Triggers" section.
4. Specify the schedule using cron syntax.

### Cron Syntax Examples

- `H 2 * * 1-5` - Every weekday at 2 AM.
- `H/15 * * * *` - Every 15 minutes.
- `H 4 * * 0` - Every Sunday at 4 AM.
- `H 22 * * 1` - Every Monday at 10 PM.

### Example

For a build that runs every day at midnight:
- `H 0 * * *`

## Pipeline Stages Explanation

### Environment

The `environment` block sets up environment variables used throughout the pipeline.

```groovy
environment {
    ALLURE_HOME = '/opt/allure-2.13.8'
    ALLURE_CMD = "${ALLURE_HOME}/bin/allure"
    PATH = "/var/lib/jenkins/.local/bin:$PATH"
    BASE_URL = 'https://your-app-url'
}
```

### Install Dependencies

This stage ensures that essential tools and libraries are installed on the Jenkins agent.

```
stage('Install Dependencies') {
    steps {
        sh 'which google-chrome'
        sh 'which git'
        sh 'python3 -m pip --version'
    }
}
```

### Checkout
This stage checks out the project code from the Git repository.

```
stage('Checkout') {
    steps {
        git url: 'https://github.com/bersh92/orangeHrm.git', branch: 'master'
    }
}
```

### Setup Python
This stage sets up the Python environment by upgrading pip and installing required dependencies from requirements.txt.

```
stage('Setup Python') {
    steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'pip3 install -r requirements.txt'
    }
}
```
### Verify pytest Installation
This stage verifies that pytest is installed correctly.

```
stage('Verify pytest Installation') {
    steps {
        sh 'which pytest'
        sh 'pytest --version'
    }
}
```

### Create .env File with Jenkins Credentials
This stage creates a `.env` file with the necessary credentials for running the tests, using Jenkins credentials.

```
stage('Create .env File with Jenkins Credentials') {
    steps {
        withCredentials([usernamePassword(credentialsId: 'orangehrm-credentials', usernameVariable: 'USERNAME_TEST', passwordVariable: 'PASSWORD')]) {
            script {
                def envContent = """
USERNAME_TEST=${USERNAME_TEST}
PASSWORD=${PASSWORD}
BASE_URL=https://your-app-url
"""
                writeFile file: '.env', text: envContent
                sh 'cat .env'  // Print .env file contents for verification
            }
        }
    }
}
```

### Run Tests
This stage runs the tests using a custom Python script `(runner.py)`, with options for running in headless mode and in parallel.

```
stage('Run Tests') {
    steps {
        script {
            def headless = '--headless'
            def parallel = params.PARALLEL ? '--parallel' : ''
            sh '''
                echo "Running tests with the following environment variables:"
                cat .env

                # Run the tests
                python3 runner.py testHeadless ${headless} ${parallel}
            '''
        }
    }
}
```

### Generate Allure Report
This stage generates an Allure report from the test results, preserving history if available.

```
stage('Generate Allure Report') {
    steps {
        script {
            if (fileExists('allure-report/history')) {
                sh '''
                    echo "Previous history found, copying to allure-results"
                    cp -r allure-report/history allure-results/
                    echo "Contents of allure-results/history after copy:"
                    ls -la allure-results/history
                '''
            } else {
                echo "No previous history found"
            }
        }
        sh '''
            ${ALLURE_CMD} generate allure-results -o allure-report --clean
            echo "Contents of allure-report/history after generation:"
            ls -la allure-report/history
        '''
    }
}
```

### Generate Allure Report
This stage generates an Allure report from the test results, preserving history if available.

```
stage('Generate Allure Report') {
    steps {
        script {
            if (fileExists('allure-report/history')) {
                sh '''
                    echo "Previous history found, copying to allure-results"
                    cp -r allure-report/history allure-results/
                    echo "Contents of allure-results/history after copy:"
                    ls -la allure-results/history
                '''
            } else {
                echo "No previous history found"
            }
        }
        sh '''
            ${ALLURE_CMD} generate allure-results -o allure-report --clean
            echo "Contents of allure-report/history after generation:"
            ls -la allure-report/history
        '''
    }
}
```

### Post Actions
The post block specifies actions that should always be executed after the main pipeline stages.

```
post {
    always {
        // Save the history for the next build
        archiveArtifacts artifacts: 'allure-report/history/**', allowEmptyArchive: true
        archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
        publishHTML(target: [
            reportName: 'Allure Report',
            reportDir: 'allure-report',
            reportFiles: 'index.html',
            keepAll: true,
            alwaysLinkToLastBuild: true,
            allowMissing: false
        ])
        emailext(
            subject: "${currentBuild.currentResult}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
            body: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]': ${currentBuild.currentResult}",
            recipientProviders: [[$class: 'DevelopersRecipientProvider']]
        )
    }
}
```

## Complete Jenkins Pipeline Script

```
pipeline {
    agent any

    parameters {
        booleanParam(name: 'PARALLEL', defaultValue: false, description: 'Run tests in parallel')
    }

    environment {
        ALLURE_HOME = '/opt/allure-2.13.8'
        ALLURE_CMD = "${ALLURE_HOME}/bin/allure"
        PATH = "/var/lib/jenkins/.local/bin:$PATH"
        BASE_URL = 'https://your-app-url'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    def result = sh(script: 'which google-chrome && which git && python3 -m pip --version', returnStatus: true)
                    if (result != 0) {
                        error "Dependency installation failed"
                    }
                }
            }
        }
        stage('Checkout') {
            steps {
                git url: 'https://github.com/bersh92/orangeHrm.git', branch: 'master'
            }
        }
        stage('Setup Python') {
            steps {
                script {
                    def result = sh(script: 'python3 -m pip install --upgrade pip && pip3 install -r requirements.txt', returnStatus: true)
                    if (result != 0) {
                        error "Python setup failed"
                    }
                }
            }
        }
        stage('Create .env File with Jenkins Credentials') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'orangehrm-credentials', usernameVariable: 'USERNAME_TEST', passwordVariable: 'PASSWORD')]) {
                    script {
                        def envContent = """
USERNAME_TEST=${USERNAME_TEST}
PASSWORD=${PASSWORD}
BASE_URL=${BASE_URL}
"""
                        writeFile file: '.env', text: envContent
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def headless = '--headless'
                    def parallel = params.PARALLEL ? '--parallel' : ''
                    def command = "python3 runner.py testHeadless ${headless} ${parallel}"
                    def result = sh(script: command, returnStatus: true)
                    if (result != 0) {
                        currentBuild.result = 'FAILURE'
                        error "Tests failed"
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                // Ensure Allure results are generated even if tests fail
                try {
                    if (fileExists('allure-report/history')) {
                        sh 'cp -r allure-report/history allure-results/'
                    }
                    sh '${ALLURE_CMD} generate allure-results -o allure-report --clean'
                } catch (Exception e) {
                    echo "Failed to generate Allure report: ${e.getMessage()}"
                }

                archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
                publishHTML(target: [
                    reportName: 'Allure Report',
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
        failure {
            script {
                echo 'One or more tests failed. Check the Allure Report for details.'
            }
        }
    }
}
```