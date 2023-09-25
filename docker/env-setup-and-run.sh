#!/bin/bash

# This script is used to setup the environment and run the application

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

# Run the application
docker-compose up -d

# Check if the application is running
if [ "$(docker ps -q -f name=glue_jupyter_lab)" ]; then
  echo "Jupyter Notebook is running at http://localhost:8888"
else
  echo "Jupyter Notebook is not running. Please check the logs and try again."
fi

# Exit the script
exit 0
