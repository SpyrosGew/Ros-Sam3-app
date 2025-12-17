import os
import zmq
import cv2
import numpy as np

SERVER_IP = os.getenv("ZMQ_SERVER_IP")
PORT = os.getenv("ZMQ_SERVER_PORT", "5555")

assert SERVER_IP is not None, "ZMQ_SERVER_IP not set"

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect(f"tcp://{SERVER_IP}:{PORT}")
sock.setsockopt(zmq.SUBSCRIBE, b"realsense")

print(f"[SUB] Connected to {SERVER_IP}:{PORT}")

while True:
    topic, color_bytes, depth_bytes, ts = sock.recv_multipart()

    color = cv2.imdecode(
        np.frombuffer(color_bytes, np.uint8),
        cv2.IMREAD_COLOR
    )
    depth = cv2.imdecode(
        np.frombuffer(depth_bytes, np.uint8),
        cv2.IMREAD_UNCHANGED
    )

    cv2.imshow("RGB", color)
    cv2.imshow("Depth", depth * 0.03)
    cv2.waitKey(1)
