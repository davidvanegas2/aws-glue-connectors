#!/bin/bash

# This script is used to setup the environment and run the application

# Load the environment variables from the config.sh file
source ./config.sh

# Run the application
docker-compose -f ./docker-compose.yml -f ./spark_submit/docker-compose.spark.yml up -d

# Check if the application is running
if [ "$(docker ps -q -f name=glue_spark_submit)" ]; then
  echo "spark-submit is running"
else
  echo "spark-submit didn't run. Please check the logs and try again."
fi

# Exit the script
exit 0
