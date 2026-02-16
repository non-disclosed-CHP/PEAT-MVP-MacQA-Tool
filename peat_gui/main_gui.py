from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PEAT MVP Demo")
        self.setGeometry(100, 100, 500, 350)

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
            self.label.setText(f"Loaded video: {os.path.basename(file_path)}")

    def annotate_frame(self):
        QMessageBox.information(self, "Annotation", "Frame annotated successfully!")

    def export_annotations(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Annotations", "", "Text Files (*.txt)")
        if save_path:
            with open(save_path, 'w') as f:
                f.write("Demo annotation data\n")
            QMessageBox.information(self, "Export", f"Annotations saved to {save_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
