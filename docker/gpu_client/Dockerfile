FROM osrf/ros:humble-desktop

LABEL maintainer="Your Name"
LABEL description="ROS 2 Humble GPU client with CycloneDDS for multi-machine."

# Install CycloneDDS + ROS 2 CLI
RUN apt-get update && apt-get install -y \
    ros-humble-rmw-cyclonedds-cpp \
    ros-humble-ros-base \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/ros_entrypoint.sh"]

# Default command: interactive shell
CMD ["bash"]
