# remote-controller
A remote controlling system that I used when running the M-4 ship.

# gstreamer command
```shell
gst-launch-1.0 -v udpsrc port=5000 ! application/x-rtp,encoding-name=H264 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink
```

conda解除忘れ注意!