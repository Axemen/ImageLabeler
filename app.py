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

        self.type = 'multiclass'
        self.classes = ['one', 'two', 'three', 'four', 'five', 'six']
        self.controls = MCControls(self.classes)

        self.controls.next.clicked.connect(self.next_path)
        self.controls.prev.clicked.connect(self.prev_path)
        self.controls.tagImage.connect(self.on_tagImage)

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
        else:
            return self.msgbox.error("There is no next")

        if not self.type == 'binary':
            print("n")
            self.controls.updateButtons(self.data[self.index])

    def prev_path(self):
        if self.index - 1 >= 0:
            self.index -= 1
            self.imageViewer.diplayImage(self.paths[self.index])

        if not self.type == 'binary':
            print('p')
            self.controls.updateButtons(self.data[self.index])

    def build_data(self):
        if self.type == 'binary':
            self.data = [{'path': p, 'tagged': 0} for p in self.paths]

        if self.type == 'multiclass':
            self.data = [{'path': p, 'class': None} for p in self.paths]

        if self.type == 'multilabel':
            self.data = []
            for p in self.paths:
                d = {'path': p}
                for c in self.classes:
                    d[c] = 0
                self.data.append(d)

    def on_tagImage(self):
        if self.type == 'binary':
            if self.data[self.index]['tagged']:
                self.data[self.index]['tagged'] = 0
            else:
                self.data[self.index]['tagged'] = 1

        if self.type == 'multiclass':
            c = [b.text() for b in self.controls.btn_group.buttons()
                 if b.isChecked()][0]
            if c:
                self.data[self.index]['class'] = c
            else:
                self.data[self.index]['class'] = None

        if self.type == 'multilabel':
            d = {b.text(): int(b.isChecked())
                 for b in self.controls.btn_group.buttons()}
            d['path'] = self.data[self.index]['path']
            self.data[self.index] = d

        print(self.data[self.index])

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
