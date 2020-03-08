#!/bin/bash

finish() {
    # Fix ownership of output files
    user_id=$(stat -c '%u:%g' /data)
    chown -R ${user_id} /data
}

echo "Started Experiment Container"

# python3 app/app.py