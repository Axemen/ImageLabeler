import sys
from pathlib import Path

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from widgets import *

VALID_FILE_EXTENSIONS = ['.jpg', '.png', '.tiff', '.bmp', '.jpeg', '.gif',
                         '.pbm', '.pgm', '.ppm', '.xbm', '.xpm']


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.imageViewer = ImageViewer()
        self.msgbox = MsgBox()

        self.type = 'binary'
        self.controls = BinaryControls(self)
        
        self.controls.next.clicked.connect(self.next_path)
        self.controls.prev.clicked.connect(self.prev_path)
        self.controls.tagImage.clicked.connect(self.on_tagImage)

        self.controls.setMaximumHeight(100)

        self.load_files()

        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.imageViewer)
        layout.addWidget(self.controls)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_files(self):
        self.paths = [str(p) for p in Path("E:/images").glob("*.*")]
        self.index = 0
        self.imageViewer.diplayImage(self.paths[self.index])
        self.build_data()

    def next_path(self):
        if self.index + 1 <= len(self.paths):
            self.index += 1
            self.imageViewer.diplayImage(self.paths[self.index])

    def prev_path(self):
        if self.index - 1 >= 0:
            self.index -= 1
            self.imageViewer.diplayImage(self.paths[self.index])

    def build_data(self):
        if self.type == 'binary':
            self.data = [{'path':p, 'tagged':0} for p in self.paths]
        # TODO add other types

    def on_tagImage(self):
        if self.type == 'binary':
            if self.data[self.index]['tagged']:
                self.data[self.index]['tagged'] = 0
            else:
                self.data[self.index]['tagged'] = 1

        print(self.data[self.index]['tagged'])

        # TODO add other types



if __name__ == "__main__":
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
        sys.exit()
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.move(500, 100)
    widget.resize(800, 800)
    app.exec_()
