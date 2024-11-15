# Use the official Python 3.12 slim image as a base image
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all project files from the local directory to /app in the container
COPY . /app

# Install the required Python Pips from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Scores.txt file from the local directory to the root of the container
COPY Scores.txt /Scores.txt

# environment variable Flask to listen on all available network interfaces (not just localhost)
# This allows the app to be accessible from outside the container
ENV FLASK_RUN_HOST=0.0.0.0

# This will start the Flask server when the container is run
CMD ["python", "main_score.py"]
