from os import remove
import sys
from pathlib import Path
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sip

from widgets import *

VALID_FILE_EXTENSIONS = ['.jpg', '.png', '.tiff', '.bmp', '.jpeg', '.gif',
                         '.pbm', '.pgm', '.ppm', '.xbm', '.xpm']


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.create_menu()

        self.imageViewer = ImageViewer()
        self.msgbox = MsgBox()

        self.controls = BinaryControls()

        self.controls.next.clicked.connect(self.next_path)
        self.controls.prev.clicked.connect(self.prev_path)

        self.controls.setMaximumHeight(100)

        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.imageViewer)
        layout.addWidget(self.controls)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_files(self):
        self.paths = [str(p) for p in Path("E:/images").glob("*.*")]
        self.controls.buildData(self.paths)
        self.imageViewer.diplayImage(
            self.controls.data[self.controls.index]['path'])

    def next_path(self):
        if self.controls.index + 1 < len(self.controls.data):
            self.controls.index += 1
            self.imageViewer.diplayImage(
                self.controls.data[self.controls.index]['path'])
        else:
            return self.msgbox.critical("There is no next")

        self.controls.updateButtons(self.controls.data[self.controls.index])

    def prev_path(self):
        if self.controls.index - 1 >= 0:
            self.controls.index -= 1
            self.imageViewer.diplayImage(
                self.controls.data[self.controls.index]['path'])
        else:
            return self.msgbox.critical("There is no previous")

        self.controls.updateButtons(self.controls.data[self.controls.index])

    def create_menu(self):
        file = self.menuBar().addMenu("File")

        loadData = QAction("Load Images", self)
        loadData.triggered.connect(self.load_files)
        file.addAction(loadData)

        exportData = QAction("Export Tags", self)
        exportData.triggered.connect(self.export_data)
        file.addAction(exportData)

        tagType = self.menuBar().addMenu("Tagger")

        binary = QAction("Binary", self)
        binary.triggered.connect(self.change_to_binary)
        tagType.addAction(binary)

        mc = QAction("Multi-Class", self)
        mc.triggered.connect(self.change_to_multi_class)
        tagType.addAction(mc)

        ml = QAction("Multi-Label", self)
        ml.triggered.connect(self.change_to_multi_label)
        tagType.addAction(ml)

    def export_data(self) -> None:
        path = QFileDialog.getSaveFileName(self, "Save Tags", ".", "(*.json)")
        if not path:
            return

        json.dump(self.controls.data, open(path[0], 'w'))

    def change_to_binary(self):
        self.centralWidget().layout().removeWidget(self.controls)
        sip.delete(self.controls)
        self.imageViewer.resetImage()

        self.controls = BinaryControls()
        self.controls.next.clicked.connect(self.next_path)
        self.controls.prev.clicked.connect(self.prev_path)
        self.controls.setMaximumHeight(100)

        if hasattr(self, 'paths'):
            self.controls.buildData(self.paths)
            self.imageViewer.diplayImage(
                self.controls.data[0]['path'])

        self.centralWidget().layout().addWidget(self.controls)

    def change_to_multi_class(self):
        def init():
            # Grabbing classes
            classes = self.selector.classes.text()
            classes = [c.strip() for c in classes.split(',')]

            # Removing popup
            sip.delete(self.selector)

            self.centralWidget().layout().removeWidget(self.controls)
            sip.delete(self.controls)
            self.imageViewer.resetImage()

            self.controls = MultiClassControls(classes)
            self.controls.next.clicked.connect(self.next_path)
            self.controls.prev.clicked.connect(self.prev_path)
            self.controls.setMaximumHeight(100)

            if hasattr(self, 'paths'):
                self.controls.buildData(self.paths)
                self.imageViewer.diplayImage(
                    self.controls.data[0]['path'])

            self.centralWidget().layout().addWidget(self.controls)

        self.selector = ClassSelector()
        self.selector.submit.clicked.connect(init)

        

    def change_to_multi_label(self):
        def init():
            # Grabbing classes
            classes = self.selector.classes.text()
            classes = [c.strip() for c in classes.split(',')]

            # Removing popup
            sip.delete(self.selector)

            self.centralWidget().layout().removeWidget(self.controls)
            sip.delete(self.controls)
            self.imageViewer.resetImage()

            self.controls = MultiLabelControls(classes)
            self.controls.next.clicked.connect(self.next_path)
            self.controls.prev.clicked.connect(self.prev_path)
            self.controls.setMaximumHeight(100)

            if hasattr(self, 'paths'):
                self.controls.buildData(self.paths)
                self.imageViewer.diplayImage(
                    self.controls.data[0]['path'])

            self.centralWidget().layout().addWidget(self.controls)

        self.selector = ClassSelector()
        self.selector.submit.clicked.connect(init)


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
