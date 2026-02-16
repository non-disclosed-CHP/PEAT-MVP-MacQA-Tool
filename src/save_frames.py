import cv2
import os

video_dir = os.path.expanduser("~/PEAT-MVP-MacQA-Tool/assets")
output_dir = os.path.expanduser("~/PEAT-MVP-MacQA-Tool/frames")  # <- absolute path

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(video_dir):
    if file_name.endswith(".mp4"):
        video_path = os.path.join(video_dir, file_name)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_name = f"{os.path.splitext(file_name)[0]}_frame_{frame_count:04d}.png"
            cv2.imwrite(os.path.join(output_dir, frame_name), frame)
            frame_count += 1
        print(f"{file_name} - Saved {frame_count} frames to {output_dir}")
        cap.release()
