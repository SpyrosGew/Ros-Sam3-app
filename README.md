This project contains multiple services you need to run, which are listed in the docker-compose.yml file.

## Service 1: sensor_node

sensor_node with the realsense_node container is responsible for gathering data from a realsense camera and publishing streams in the form of ROS topics.

You can enter the running container for testing with

```console
sudo docker exec -it realsense_node bash -c "source /opt/ros/humble/setup.bash && ros2 topic list"
```

