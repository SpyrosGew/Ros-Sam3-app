This project contains multiple services you need to run, which are listed in the docker-compose.yml file.

## Service 1: sensor_node

sensor_node with the realsense_node container is responsible for gathering data from a realsense camera and publishing streams in the form of ROS topics.

On the host machine, you need to install the Realsense udev Rules. These are specific USB device rules for RealSense so the container can get the correct permissions to access the camera.


```console
# Clone the repository (you can remove this directory later if you wish)
git clone https://github.com/IntelRealSense/librealsense.git
```

```console
cd librealsense/config
sudo cp 99-realsense-libusb.rules /etc/udev/rules.d/
```
Reload the udev daemon

```console
sudo udevadm control --reload-rules
sudo udevadm trigger
```

You should connect the camera to the host machine before you run the container. You can see if your host machine sees the camera with

```console
lsusb
```

You can enter the running container for testing with

```console
sudo docker exec -it realsense_node bash -c "source /opt/ros/humble/setup.bash && ros2 topic list"
```

