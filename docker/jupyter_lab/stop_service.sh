#!/bin/bash

# This script is used to stop the Docker Compose service

# Load the environment variables from the config.sh file
source ./config.sh

# Check if the application is running
if [ "$(docker ps -q -f name=glue_jupyter_lab)" ]; then
  echo "Jupyter Notebook is running at http://localhost:8888"
else
  echo "Jupyter Notebook is not running. It's not necessary to stop the service."
  exit 1
fi

# Stop the application
docker-compose -f ./docker-compose.yml -f ./jupyter_lab/docker-compose.jupyter.yml down -v

# Check if the application is stopped
if [ "$(docker ps -q -f name=glue_jupyter_lab)" ]; then
  echo "Jupyter Notebook is still running. Please check the logs and try again."
else
  echo "Jupyter Notebook is stopped."
fi

# Exit the script
exit 0
