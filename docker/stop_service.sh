#!/bin/bash

# This script is used to stop the Docker Compose service

# Load the environment variables from the config.sh file
source ./config.sh

# Check if Docker is installed
if ! [ -x "$(command -v docker)" ]; then
  echo "Docker is not installed. Please install Docker and try again."
  exit 1
fi

# Check if Docker Compose is installed
if ! [ -x "$(command -v docker-compose)" ]; then
  echo "Docker Compose is not installed. Please install Docker Compose and try again."
  exit 1
fi

# Stop the application
docker-compose down -v

# Check if the application is stopped
if [ "$(docker ps -q -f name=glue_jupyter_lab)" ]; then
  echo "Jupyter Notebook is still running. Please check the logs and try again."
else
  echo "Jupyter Notebook is stopped."
fi

# Exit the script
exit 0
