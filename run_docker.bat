@echo off

rem Build the Docker image
docker build -t my-flask-app .

rem Run the Docker container
docker run -p 5000:5000 my-flask-app
