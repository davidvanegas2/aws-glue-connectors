#!/bin/bash

# This script is used to define the variables used in the Docker Compose service to run Glue locally

# Determine the current directory
CURRENT_DIR=$(dirname "$0")

# Define the variables
export JUPYTER_WORKSPACE_LOCATION="$CURRENT_DIR/../.."
export PROFILE_NAME="default" # It needs to be changed to the name of the profile you want to use

# Verify the values of the environment variables
echo "JUPYTER_WORKSPACE_LOCATION: $JUPYTER_WORKSPACE_LOCATION"
echo "PROFILE_NAME: $PROFILE_NAME"
