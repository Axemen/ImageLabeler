import sys
from pathlib import Path

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from widgets.msgbox import MsgBox
from widgets.image_viewer import ImageViewer


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.imageViewer = ImageViewer()

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
        sys.exit()
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.move(500, 200)
    widget.resize(800, 800)
    app.exec_()
