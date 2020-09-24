from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageViewer(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.view = QLabel()
        self.view.setMinimumSize(1, 1)
        layout.addWidget(self.view)

        self.view.setStyleSheet("background-color: yellow")

        self.setLayout(layout)

    def resizeEvent(self, event):
        try:
            self.setImage(self.image)
            self.view.adjustSize()

        except AttributeError:
            pass
        super().resizeEvent(event)

    def diplayImage(self, path):
        self.image = QImage(path)
        self.setImage(self.image)

    def setImage(self, image):
        self.scaled_image = self.image.scaled(self.view.size())
        self.view.setPixmap(QPixmap.fromImage(self.scaled_image))


class BottomBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("BottomBar")

        self.next = QPushButton('Next')
        self.prev = QPushButton("Previous")

        layout = QHBoxLayout()        

        

        layout.addWidget(self.prev)
        layout.addWidget(self.next)

        self.setLayout(layout)


class MsgBox(QWidget):

    def __init__(self):
        super().__init__()

    def error(self, msg):
        pass

    def warning(self, msg):
        pass

    def info(self, msg):
        pass
