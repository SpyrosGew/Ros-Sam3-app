FROM osrf/ros:foxy-desktop

LABEL description="ROS 2 Foxy container for RealSense D400 series with FastDDS."

# Install RealSense ROS 2 wrapper and Fast DDS
RUN apt-get update && apt-get install -y \
    ros-foxy-realsense2-camera \
    ros-foxy-rmw-fastrtps-cpp \
    usbutils \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["ros2", "launch", "realsense2_camera", "rs_launch.py"]