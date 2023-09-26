#!/bin/bash

# This script is used to stop the Docker Compose service

# Load the environment variables from the config.sh file
source ./config.sh

# Check if the application is running
if [ "$(docker ps -q -f name=glue_spark_submit)" ]; then
  echo "spark-submit is running"
else
  echo "spark-submit is not running. It's not necessary to stop the service."
  exit 1
fi

# Stop the application
docker-compose -f ./docker-compose.yml -f ./spark_submit/docker-compose.spark.yml down -v

# Check if the application is stopped
if [ "$(docker ps -q -f name=glue_spark_submit)" ]; then
  echo "spark-submit is still running. Please check the logs and try again."
else
  echo "spark-submit is stopped."
fi

# Exit the script
exit 0
