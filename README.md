# remote-controller
A remote controlling system that I used when running the M-4 ship.

# initializing ship pi
The following programs are required to run this remote controlling system.
- Git
- python3
- pip3
- Gstreamer
- Utils for Gstreamer
We install all of these by the following command
```shell
sudo apt update
sudo apt install -y python3 python3-pip git gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
```

In addition, in order to use pyserial, we install them via pip3.

```shell
pip3 install pyserial
```

# gstreamer command
```shell
gst-launch-1.0 -v udpsrc port=5000 ! application/x-rtp,encoding-name=H264 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink
```
This command is for the land receiver, which will have to have gstreamer installed.

# background process command
```shell
nohup [[process name]] output.log 2>&1 &
```

For example:
```shell
nohup bash start_gstreamer.sh > gstreamer.log 2>&1 &
```

Under the ship folder, there will be a start command that starts everything you need for this project, while wrapping the command around with the nohup command in order to prevent process stopping from termination of the terminal.

# ship side

When using an FRC Camera, the following command worked instead of the command written in the ship folder

```shell
gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay config-interval=1 ! udpsink host=$RECEIVER_IP port=$PORT
```