pipeline {
    agent any

    environment {
        // Docker image name on DockerHub
        DOCKER_IMAGE = 'amitgrin/world-of-games'
        DOCKER_TAG = 'latest'  // You can use a specific version or date here
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the repository
                    echo 'Checking out repository...'
                    git branch: 'main', url: 'https://github.com/Grinberg-stack/World-Of-Games.git'  // Replace with your GitHub repository URL
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile
                    echo 'Building Docker image...'
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")  // Build the image from the Dockerfile
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container, mapping port 8777 and mounting the Scores.txt file
                    echo 'Running Docker container...'
                    // Use quotes to handle paths with spaces
                    bat """
                    docker run -d -p 8777:8777 -v \"${pwd()}/Scores.txt\":/Scores.txt --name score_app ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    // Install Python dependencies from requirements.txt
                    echo 'Installing dependencies...'
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run Selenium tests with e2e.py
                    echo 'Running Selenium tests...'
                    bat 'python tests/e2e.py'  // Run the Selenium script
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop the running Docker container
                    echo 'Stopping Docker container...'
                    bat 'docker stop score_app'  // Stop the container
                    bat 'docker rm score_app'    // Remove the container

                    // Push the newly built image to DockerHub
                    echo 'Pushing Docker image to DockerHub...'
                    bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"  // Push the image to DockerHub
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker resources after pipeline execution
            echo 'Cleaning up Docker resources...'
            bat 'docker system prune -f'  // Remove unused images and containers
        }
    }
}