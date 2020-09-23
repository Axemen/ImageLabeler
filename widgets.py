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


class BottomBar(QWidget):

    _next = pyqtSignal()
    _prev = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

        self.next = QPushButton('Next')
        self.prev = QPushButton("Previous")

        layout = QHBoxLayout()

        layout.addWidget(self.prev)
        layout.addWidget(self.next)


class MsgBox(QWidget):
    def __init__(self):
        super().__init__()

    def error(self, msg):
        pass

    def warning(self, msg):
        pass

    def info(self, msg):
        pass
