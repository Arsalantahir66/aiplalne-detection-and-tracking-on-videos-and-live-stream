from collections import defaultdict
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# Dictionary to store tracking history with default empty lists
track_history = defaultdict(lambda: [])

# Load the YOLO model
model = YOLO("yolov8l.pt")

# Open the video file
cap = cv2.VideoCapture("IMG_7672.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Initialize video writer to save the output video with the specified properties
out = cv2.VideoWriter("aircraft-detection.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

while True:
    ret, im0 = cap.read()
    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    annotator = Annotator(im0, line_width=2)
    results = model.track(im0, persist=True)
    if results[0].boxes.id is not None and results[0].boxes.xyxy is not None:
        bboxes = results[0].boxes.xyxy
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()
        for bbox, track_id in zip(bboxes, track_ids):
            label=f"aircraft :{track_id}"
            annotator.box_label(bbox, label, color=colors(track_id, True))
    out.write(im0)
