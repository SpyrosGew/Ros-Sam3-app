This project contains multiple services you need to run, which are listed in the docker-compose.yml file.

## Service 1: sensor_node and Discovery Server (your laptop)

sensor_node with the realsense_node container is responsible for gathering data from a realsense camera and publishing streams with zeroMQ.

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

Build the sensor node on you laptop with

```console
docker compose --profile pc1 build
```

And run it with

```console
docker compose --profile pc1 up -d
```

Check the logs for any errors (most importantly if the container is connected to the RealSense device) with

```console
sudo docker logs realsense_node
```


## Service 2: gpu client (the service that should recieve the topics)

```console
docker compose --profile pc2 build

```

```console
docker compose --profile pc2 up -d
```




