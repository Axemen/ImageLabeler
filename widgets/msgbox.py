from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

class MsgBox(QWidget):
    def __init__(self):
        super().__init__()

    def error(self, msg):
        pass

    def warning(self, msg):
        pass

    def info(self, msg):
        pass
        