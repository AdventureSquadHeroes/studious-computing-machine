#!/bin/bash

# Build the Docker image
docker build -t my-flask-app .

# Run the Docker container
docker run -p 5000:5000 my-flask-app
