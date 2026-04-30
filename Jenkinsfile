pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY = 'demo-app'
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
                echo 'Installing Python dependencies...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests with coverage...'
                sh '''
                    python3 -m pytest test_app.py \
                        --cov=app \
                        --cov-report=xml:coverage.xml \
                        --cov-report=term-missing \
                        -v
                '''
            }
            post {
                always {
                    echo 'Test stage complete.'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube code quality scan...'
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                            -Dsonar.projectName="Demo App" \
                            -Dsonar.sources=. \
                            -Dsonar.language=py \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
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