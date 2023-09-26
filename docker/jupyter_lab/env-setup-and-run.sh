#!/bin/bash

# This script is used to setup the environment and run the application

# Load the environment variables from the config.sh file
source ./config.sh

# Run the application
docker-compose -f ./docker-compose.yml -f ./jupyter_lab/docker-compose.jupyter.yml up -d

# Check if the application is running
if [ "$(docker ps -q -f name=glue_jupyter_lab)" ]; then
  echo "Jupyter Notebook is running at http://localhost:8888"
else
  echo "Jupyter Notebook is not running. Please check the logs and try again."
fi

# Exit the script
exit 0
