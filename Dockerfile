# Use the official Python 3.12 slim image as a base image
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all project files from the local directory to /app in the container
COPY . /app

# Install the required Python packages from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Scores.txt file from the local directory to the root of the container
COPY Scores.txt /Scores.txt

# Set environment variables for Flask
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8777

# Start the Flask server directly (without Gunicorn)
CMD ["python", "main_score.py"]

# Expose the port so Docker knows the app will be using it
EXPOSE 8777