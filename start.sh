#!/bin/bash

# This script will run our long gunicorn command
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:21904 main:app
