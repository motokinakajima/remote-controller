PORT="5000"

gst-launch-1.0 -v udpsrc port=$PORT ! application/x-rtp,encoding-name=H264 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink