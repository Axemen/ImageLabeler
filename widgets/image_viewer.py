from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.view = QLabel()
        layout.addWidget(self.view)

        self.setLayout(layout)


    def display_image(self, path):
        image = QImage(path)
        if (image.height() > self.view.height()) and (image.width() > self.view.width()):
            image.scaled(self.view.size())

        elif image.height() > self.view.height():
            image.scaledToHeight(self.view.height())

        elif image.width() > self.view.width():
            image.scaledToWidth(self.view.width())

        self.view.setPixmap(QPixmap.fromImage(image))
