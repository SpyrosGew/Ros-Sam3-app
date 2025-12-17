import os
import time
import zmq
import cv2
import numpy as np
import pyrealsense2 as rs

# ZeroMQ config
PORT = os.getenv("ZMQ_PUB_PORT", "5555")

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind(f"tcp://*:{PORT}")

# RealSense setup
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

print(f"[PUB] Streaming on port {PORT}")

try:
    while True:
        frames = pipeline.wait_for_frames()
        color = np.asanyarray(frames.get_color_frame().get_data())
        depth = np.asanyarray(frames.get_depth_frame().get_data())

        _, color_jpg = cv2.imencode(".jpg", color, [cv2.IMWRITE_JPEG_QUALITY, 80])
        _, depth_png = cv2.imencode(".png", depth)

        sock.send_multipart([
            b"realsense",
            color_jpg.tobytes(),
            depth_png.tobytes(),
            str(time.time_ns()).encode()
        ])

except KeyboardInterrupt:
    pass
finally:
    pipeline.stop()
