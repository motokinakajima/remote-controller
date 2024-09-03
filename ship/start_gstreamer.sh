#!/bin/bash

# Shell script to send camera stream via UDP using GStreamer

# IP address of the receiving device (replace with the receiver's IP)
RECEIVER_IP="192.168.1.19"
PORT="5000"

# Start the GStreamer pipeline to capture, encode, and send the stream
gst-launch-1.0 -v v4l2src device=/dev/video0 ! video/x-raw,width=320,height=240,framerate=15/1 ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay config-interval=1 ! udpsink host=$RECEIVER_IP port=$PORT

