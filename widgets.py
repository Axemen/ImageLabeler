from typing import List

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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

    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)
        self.tagImage = QPushButton("Tag")

        layout.addWidget(self.tagImage)
        layout.addWidget(self.bottomBar)

        self.setLayout(layout)


class MCControls(QWidget):
    """ Multi-class controls """

    tagImage = pyqtSignal()

    def __init__(self, classes: List[str]) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)

        self.btn_layout = QHBoxLayout()
        self.btn_group = QButtonGroup()

        self.btn_group.buttonClicked.connect(lambda _: self.tagImage.emit())

        for c in classes:
            btn = QRadioButton(c)
            self.btn_layout.addWidget(btn)
            self.btn_group.addButton(btn)

        # Extra button for None option
        btn = QRadioButton()
        self.btn_layout.addWidget(btn)
        self.btn_group.addButton(btn)

        layout.addLayout(self.btn_layout)
        layout.addWidget(self.bottomBar)

        self.setLayout(layout)

    def updateButtons(self, d):
        self.btn_group.blockSignals(True)
        for b in self.btn_group.buttons():
            if d['class'] == b.text():
                b.setChecked(True)
                break
        else:
            b.setChecked(True)
        self.btn_group.blockSignals(False)


class MLControls(QWidget):
    """ Multi-label controls """

    tagImage = pyqtSignal()

    def __init__(self, labels) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)

        self.btn_layout = QHBoxLayout()
        self.btn_group = QButtonGroup()
        self.btn_group.setExclusive(False)

        self.btn_group.buttonClicked.connect(lambda _: self.tagImage.emit())

        for label in labels:
            btn = QRadioButton(label)
            self.btn_layout.addWidget(btn)
            self.btn_group.addButton(btn)

        layout.addLayout(self.btn_layout)
        layout.addWidget(self.bottomBar)

        self.setLayout(layout)

    def updateButtons(self, d: dict):
        self.btn_group.blockSignals(True)
        for btn in self.btn_group.buttons():
            btn.setChecked(bool(d[btn.text()]))
        self.btn_group.blockSignals(False)


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
