from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


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

