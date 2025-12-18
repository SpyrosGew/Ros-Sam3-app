FROM osrf/ros:foxy-desktop

# Install base utilities + Fast DDS
RUN apt-get update && apt-get install -y \
    ros-foxy-rmw-fastrtps-cpp \
    python3-pip \
    python3-argcomplete \
    && rm -rf /var/lib/apt/lists/*

# The entrypoint is already in the base image, but we can be explicit
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]