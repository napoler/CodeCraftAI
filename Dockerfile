# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY .codecraft/requirements/dev.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r dev.txt

# Copy the rest of the application's code to the working directory
COPY . .

# Expose a port if your application is a web service
# EXPOSE 8000

# Define the command to run your application
# CMD ["python", "src/codecraftai/main.py"]
