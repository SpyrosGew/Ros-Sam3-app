# Use a ROS 2 Humble base image
FROM osrf/ros:humble-desktop

# Metadata
LABEL maintainer="Your Name"
LABEL description="ROS 2 Humble container for RealSense D400 series camera."

# Install the RealSense ROS 2 wrapper and its dependencies
RUN apt update && apt install -y \
    ros-humble-realsense2-camera \
    # Clean up after installation to keep the image small
    && rm -rf /var/lib/apt/lists/*

# Set the entrypoint to the ROS 2 setup script
ENTRYPOINT ["/ros_entrypoint.sh"]

# Default command to keep the container running if no other command is provided
CMD ["tail", "-f", "/dev/null"]