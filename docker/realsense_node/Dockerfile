FROM osrf/ros:humble-desktop

LABEL maintainer="Your Name"
LABEL description="ROS 2 Humble container for RealSense D400 series camera."

# Install RealSense ROS 2 wrapper + CycloneDDS
RUN apt-get update && apt-get install -y \
    ros-humble-realsense2-camera \
    ros-humble-rmw-fastrtps-cpp \
    && rm -rf /var/lib/apt/lists/*

# ROS 2 entrypoint
ENTRYPOINT ["/ros_entrypoint.sh"]

# Default command: interactive shell
CMD ["bash"]
