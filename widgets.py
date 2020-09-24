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

    def resizeEvent(self, event: QResizeEvent):
        try:
            self.setImage()
            self.view.adjustSize()

        except AttributeError:
            pass
        super().resizeEvent(event)

    def diplayImage(self, path):
        self.image = QImage(path)
        self.setImage()

    def setImage(self):
        self.scaled_image = self.image.scaled(self.view.size())
        self.view.setPixmap(QPixmap.fromImage(self.scaled_image))


class BottomBar(QWidget):

    def __init__(self, ctrl: QWidget):
        super().__init__()

        self.next = QPushButton('Next')
        self.prev = QPushButton("Previous")

        ctrl.next = self.next
        ctrl.prev = self.prev

        layout = QHBoxLayout()
        layout.addWidget(self.prev)
        layout.addWidget(self.next)
        self.setLayout(layout)


class BinaryControls(QWidget):

    def __init__(self, app: QMainWindow) -> None:
        super().__init__()
        self.app = app
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)
        self.tagImage = QPushButton("Tag")

        layout.addWidget(self.tagImage)
        layout.addWidget(self.bottomBar)

        self.setLayout(layout)


class MsgBox(QWidget):

    def __init__(self) -> None:
        super().__init__()

    def display(self, msg: str, type: QMessageBox.Icon) -> None:
        msgbox = QMessageBox()
        msgbox.setIcon(type)
        msgbox.setText(msg)
        msgbox.exec_()

    def critical(self, msg: str) -> None:
        self.display(msg, QMessageBox.Critical)

    def warning(self, msg: str) -> None:
        self.display(msg, QMessageBox.Warning)

    def info(self, msg: str) -> None:
        self.display(msg, QMessageBox.Information)
