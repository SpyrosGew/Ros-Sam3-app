FROM ubuntu:22.04

LABEL maintainer="Your Name"
LABEL description="RealSense ZeroMQ publisher"

ENV DEBIAN_FRONTEND=noninteractive

# System deps
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libgl1 \
    libglib2.0-0 \
    usbutils \
    && rm -rf /var/lib/apt/lists/*

# Python deps
RUN pip3 install --no-cache-dir \
    pyzmq \
    numpy \
    opencv-python \
    pyrealsense2

# Workspace
WORKDIR /app

# Copy your python publisher here
COPY realsense_publisher.py /app/realsense_publisher.py

CMD ["python3", "/app/realsense_publisher.py"]
