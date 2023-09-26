#!/bin/bash

# This script is used to run or stop Glue locally using docker-compose
# Receives a parameter as input to run Glue using: jupyter-lab or spark-submit
# Receives a parameter as input to stop Glue using: stop

# Read the input parameter
if [ $# -eq 0 ]; then
    echo "No arguments supplied. Please provide the service you want to run: jupyter-lab or spark-submit"
    exit 1
fi

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

# Check if the shell files needs execute permission
if ! [ -x ".jupyter_lab/env-setup-and-run.sh" ]; then
    chmod +x ./jupyter_lab/env-setup-and-run.sh
fi

if ! [ -x ".spark_submit/env-setup-and-run.sh" ]; then
    chmod +x ./spark_submit/env-setup-and-run.sh
fi

if ! [ -x ".jupyter_lab/stop_service.sh" ]; then
    chmod +x ./jupyter_lab/stop_service.sh
fi

# TODO: Uncomment the line below when the Spark Submit is ready
#if ! [ -x ".spark_submit/stop_service.sh" ]; then
#    chmod +x ./spark_submit/stop_service.sh
#fi

# If the parameter is jupyter-lab, it will run the file: "jupyter_lab/env-setup-and-run.sh".
# If the parameter is spark-submit, it will run the file: "spark_submit/env-setup-and-run.sh"
if [ "$1" == "jupyter-lab" ]; then
    echo "Running Jupyter Notebook"
    ./jupyter_lab/env-setup-and-run.sh
# TODO: Uncomment the line below when the Spark Submit is ready
#elif [ "$1" == "spark-submit" ]; then
#    echo "Running Spark Submit"
#    ./spark_submit/env-setup-and-run.sh
elif [ "$1" == "stop" ]; then
    echo "Stopping all services"
    ./jupyter_lab/stop_service.sh
    # TODO: Uncomment the line below when the Spark Submit is ready
#    ./spark_submit/stop_service.sh
else
    echo "Invalid argument. Please provide the service you want to run: jupyter-lab or spark-submit"
    exit 1
fi

# Exit the script
exit 0
