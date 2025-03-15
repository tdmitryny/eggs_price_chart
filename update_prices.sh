#!/bin/bash

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to the project directory
cd $DIR

# Run the Docker command to update prices
docker exec $(docker ps -q -f name=egg_chart) python manage.py update_price_data
