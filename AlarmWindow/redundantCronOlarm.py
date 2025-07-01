import sys
import os
import argparse
script_dir = os.path.dirname(__file__)
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPixmap, QPainter, QFont
from PySide6.QtCore import Qt, QTimer

class ImageWindow(QWidget):
    def __init__(self, image_path, message, time):
        super().__init__()
        self.image_path = image_path
        self.message = message
        self.time = int(time) * 1000
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.message)
        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            raise FileNotFoundError(f"Image not found: {self.image_path}")
        self.resize(pixmap.width(), pixmap.height())
        QTimer.singleShot(self.time, self.close)  # 10 seconds


    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_path)
        painter.drawPixmap(self.rect(), pixmap)
        painter.setPen(Qt.red)
        font = QFont('Arial', 48, QFont.Bold)
        painter.setFont(font)
        rect = self.rect()
        painter.drawText(rect, Qt.AlignCenter, self.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show an alarm window with image and message.")
    parser.add_argument('--image', '-i', required=True, help='Path to background image')
    parser.add_argument('--message', '-m', required=True, help='Message to display')
    parser.add_argument('--time', '-t', required=True, help='seconds of display time')
    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = ImageWindow(args.image, args.message, args.time)
    window.show()
    sys.exit(app.exec())
