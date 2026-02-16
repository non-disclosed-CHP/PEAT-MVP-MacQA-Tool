from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
import sys
import os

ANNOTATION_DIR = "annotations"

if not os.path.exists(ANNOTATION_DIR):
    os.makedirs(ANNOTATION_DIR)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PEAT MVP Demo")
        self.setGeometry(100, 100, 500, 350)
        self.video_file = None
        self.frame_count = 0

        layout = QVBoxLayout()
        self.label = QLabel("PEAT MVP Demo Running!", self)
        layout.addWidget(self.label)

        # Button 1: Load Video
        self.load_btn = QPushButton("Load Video", self)
        self.load_btn.clicked.connect(self.load_video)
        layout.addWidget(self.load_btn)

        # Button 2: Annotate Frame
        self.annotate_btn = QPushButton("Annotate Frame", self)
        self.annotate_btn.clicked.connect(self.annotate_frame)
        layout.addWidget(self.annotate_btn)

        # Button 3: Export Annotations
        self.export_btn = QPushButton("Export Annotations", self)
        self.export_btn.clicked.connect(self.export_annotations)
        layout.addWidget(self.export_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4 *.avi)")
        if file_path:
            self.video_file = file_path
            self.frame_count = 0
            self.label.setText(f"Loaded video: {os.path.basename(file_path)}")

    def annotate_frame(self):
        if not self.video_file:
            QMessageBox.warning(self, "Error", "No video loaded!")
            return
        # Simulate annotating a frame
        self.frame_count += 1
        annotation_file = os.path.join(ANNOTATION_DIR, f"frame_{self.frame_count:04d}.txt")
        with open(annotation_file, 'w') as f:
            f.write(f"Annotation for frame {self.frame_count}\n")
        self.label.setText(f"Annotated frame {self.frame_count}")
        QMessageBox.information(self, "Annotation", f"Frame {self.frame_count} annotated!")

    def export_annotations(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save All Annotations", "", "Text Files (*.txt)")
        if save_path:
            with open(save_path, 'w') as out_f:
                for fname in sorted(os.listdir(ANNOTATION_DIR)):
                    fpath = os.path.join(ANNOTATION_DIR, fname)
                    with open(fpath, 'r') as in_f:
                        out_f.write(in_f.read())
            QMessageBox.information(self, "Export", f"All annotations saved to {save_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
