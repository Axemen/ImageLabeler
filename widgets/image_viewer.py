from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.view = QLabel()

        self.setLayout(layout)

    def display_image(self, path):
        image = QImage(path)
        self.view.setPixmap(QPixmap.fromImage(image))
