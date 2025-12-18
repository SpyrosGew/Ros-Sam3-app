FROM ubuntu:22.04

LABEL maintainer="Your Name"
LABEL description="ZeroMQ + RealSense Publisher"

ENV DEBIAN_FRONTEND=noninteractive

# Install system deps
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libgl1 \
    libglib2.0-0 \
    usbutils \
    && rm -rf /var/lib/apt/lists/*

# Python deps
RUN pip3 install --no-cache-dir pyzmq numpy opencv-python pyrealsense2

WORKDIR /app
COPY realsense_publisher.py /app/realsense_publisher.py

# Run as root to ensure USB access
USER root

CMD ["python3", "/app/realsense_publisher.py"]
