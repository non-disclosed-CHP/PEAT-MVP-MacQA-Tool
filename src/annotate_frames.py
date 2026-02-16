import os

frames_dir = os.path.expanduser("~/PEAT-MVP-MacQA-Tool/frames")
annotations_dir = os.path.expanduser("~/PEAT-MVP-MacQA-Tool/annotations")

if not os.path.exists(annotations_dir):
    os.makedirs(annotations_dir)

for frame_file in os.listdir(frames_dir):
    if frame_file.endswith(".png"):
        annotation_file = os.path.join(annotations_dir, f"{frame_file}.txt")
        with open(annotation_file, "w") as f:
            f.write("label: TBD\n")
        print(f"Annotated {frame_file} -> {annotation_file}")
