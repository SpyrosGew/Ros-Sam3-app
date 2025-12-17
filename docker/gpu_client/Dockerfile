FROM ubuntu:22.04

LABEL maintainer="Your Name"
LABEL description="ZeroMQ GPU client"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    pyzmq \
    numpy \
    opencv-python

WORKDIR /app

# Copy your subscriber / inference code
COPY gpu_client.py /app/gpu_client.py

CMD ["python3", "/app/gpu_client.py"]
