#!/bin/bash

# This script is used to load data into Minio once the container is up and running

# Set minio alias
mc alias set minio http://minio:9000 "${MINIO_ACCESS_KEY}" "${MINIO_SECRET_KEY}"

# Upload data
mc cp -r /data/ minio/dummy-bucket/dummy-data

# Exit the script
exit 0
