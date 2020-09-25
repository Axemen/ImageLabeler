from pathlib import Path
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

    def resetImage(self):
        self.image = QImage()
        self.view.clear()


class BottomBar(QWidget):

    def __init__(self, ctrl: QWidget):
        super().__init__()

        self.next = QPushButton('Next')
        self.prev = QPushButton("Previous")

        self.ctrl = ctrl
        ctrl.next = self.next
        ctrl.prev = self.prev

        layout = QHBoxLayout()
        layout.addWidget(self.prev)
        layout.addWidget(self.next)
        self.setLayout(layout)


class BinaryControls(QWidget):

    index = 0
    data = []

    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)
        self.tagImage = QPushButton("Tag")
        self.tagImage.setCheckable(True)
        self.tagImage.clicked.connect(self.on_tagImage)

        layout.addWidget(self.tagImage)
        layout.addWidget(self.bottomBar)

        self.setLayout(layout)

    def buildData(self, paths: List[Path]) -> None:
        self.data = [{'path': p, 'tagged': 0} for p in paths]
        self.index = 0

    def updateButtons(self, d: dict) -> None:
        self.tagImage.blockSignals(True)

        tagged = bool(d['tagged'])
        self.tagImage.setChecked(tagged)

        self.tagImage.blockSignals(False)

    def on_tagImage(self) -> None:
        try:
            if self.data[self.index]['tagged']:
                self.data[self.index]['tagged'] = 0
            else:
                self.data[self.index]['tagged'] = 1
        except:
            pass


class MultiClassControls(QWidget):
    """ Multi-class controls """

    index = 0
    data = []

    def __init__(self, classes: List[str]) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)

        self.btn_layout = QHBoxLayout()
        self.btn_group = QButtonGroup()

        self.btn_group.buttonClicked.connect(self.on_tagImage)

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

    def buildData(self, paths: List[Path]) -> List[dict]:
        self.data = [{'path': p, 'class': None} for p in paths]

    def on_tagImage(self) -> None:
        c = [b.text() for b in self.btn_group.buttons()
             if b.isChecked()][0]
        if c:
            self.data[self.index]['class'] = c
        else:
            self.data[self.index]['class'] = None


class MultiLabelControls(QWidget):
    """ Multi-label controls """

    index = 0
    data = []

    def __init__(self, labels) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.bottomBar = BottomBar(self)
        self.labels = labels

        self.btn_layout = QHBoxLayout()
        self.btn_group = QButtonGroup()
        self.btn_group.setExclusive(False)

        self.btn_group.buttonClicked.connect(self.on_tagImage)

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

    def buildData(self, paths: List[Path]) -> List[dict]:
        data = []
        for p in paths:
            d = {'path': p}
            for label in self.labels:
                d[label] = 0
            data.append(d)
        self.data = data

    def on_tagImage(self) -> None:
        d = {b.text(): int(b.isChecked())
             for b in self.btn_group.buttons()}
        d['path'] = self.data[self.index]['path']
        self.data[self.index] = d


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

class ClassSelector(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.form = QFormLayout()
        self.classes = QLineEdit()
        self.form.addRow(QLabel("Classes"), self.classes)
        self.form.addRow(QLabel("Please enter all classes seperated by a ','"))
        self.submit = QPushButton("Submit")
        self.form.addRow(self.submit)

        self.setLayout(self.form)
        self.setGeometry(QRect(100, 100, 400, 100))
        self.show()

