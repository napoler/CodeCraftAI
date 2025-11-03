# Deployment and Operations Guide

This document provides instructions for deploying and maintaining the application.

## Docker Deployment

The recommended way to deploy this application is using Docker.

### Building the Image

To build the Docker image, run:
```bash
sudo docker build -t codecraftai:latest .
```

### Running the Container

To run the application in a container:
```bash
sudo docker run -d -p 8000:8000 --name my-app codecraftai:latest
```
