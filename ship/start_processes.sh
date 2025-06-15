#!/bin/bash
echo "Starting start_gstreamer.sh at $(date)" >> gstreamer.log
nohup bash start_gstreamer.sh >> gstreamer.log 2>&1 &
echo "start_gstreamer.sh PID: $!" >> gstreamer.log
echo "Starting server.py at $(date)" >> serverpy.log
nohup python3 server.py >> serverpy.log 2>&1 &
echo "server.py PID: $!" >> serverpy.log