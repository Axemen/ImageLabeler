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

        self.load_files()

        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.imageViewer)
        widget.setLayout(layout)
        self.setCentralWidget(self.imageViewer)

    def load_files(self):
        self.paths = [str(p) for p in Path("E:/images").glob("*")]
        self.index = 0 
        self.imageViewer.display_image(self.paths[self.index])

    def next_path(self):
        if self.index + 1 <= len(self.paths):
            self.index += 1
            self.imageViewer.display_image(self.paths[self.index])

    def previous_path(self):
        if self.index - 1 >= 0:
            self.index -= 1 
            self.imageViewer.display_image(self.paths[self.index])


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
