from collections import defaultdict
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# Dictionary to store tracking history with default empty lists
track_history = defaultdict(lambda: [])

# Load the YOLO model accrding to your system ..yolov8s.pt is small model is less accurate and yolovn.pt is nano model a little 
# accuracte rather than small and yolov8l.pt is large model with good accuracy 
model = YOLO("yolov8n.pt")

# replace the camera rtsp stream url or camera id with 0
cap = cv2.VideoCapture(0)


while True:
    ret, im0 = cap.read()
    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    annotator = Annotator(im0, line_width=2)
    results = model.track(im0, persist=True)
    if results[0].boxes.id is not None and results[0].boxes.xyxy is not None and results[0].boxes.cls is not None:
        bboxes = results[0].boxes.xyxy
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()
        for bbox, track_id, class_id in zip(bboxes, track_ids, class_ids):
            if class_id == 4:  
                label=f"aircraft :{track_id}"
                annotator.box_label(bbox, label, color=colors(track_id, True))
    cv2.imshow("object-detection-object-tracking", im0)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Release the video writer and capture objects, and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
