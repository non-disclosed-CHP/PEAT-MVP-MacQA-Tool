import cv2
import os

video_path = os.path.expanduser("~/PEAT-MVP-MacQA-Tool/assets/sample.mp4")
cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1

print(f"Total frames: {frame_count}")
cap.release()
