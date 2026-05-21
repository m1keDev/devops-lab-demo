pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY = 'devops-lab-demo'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling source code from GitHub...'
                checkout scm
                echo "Building commit: ${env.GIT_COMMIT}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests with coverage...'
                sh '''
                    . venv/bin/activate
                    python3 -m pytest test_app.py \
                        --cov=app \
                        --cov-report=xml:coverage.xml \
                        --cov-report=term-missing \
                        --junitxml=test-results.xml \
                        -v
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                    echo 'Test stage complete.'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube code quality scan...'
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        . venv/bin/activate
                        sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                            -Dsonar.projectName="DevOps Lab Demo" \
                            -Dsonar.sources=app.py,calculator.py,database.py,utils.py \
                            -Dsonar.tests=test_app.py \
                            -Dsonar.python.version=3 \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.exclusions=venv/**,test-results.xml \
                            -Dsonar.scm.revision=${GIT_COMMIT}
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Checking SonarQube quality gate result...'
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

    }

    post {
        success {
            echo "Pipeline PASSED — commit ${env.GIT_COMMIT} is clean."
        }
        failure {
            echo "Pipeline FAILED — commit ${env.GIT_COMMIT} needs attention."
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}