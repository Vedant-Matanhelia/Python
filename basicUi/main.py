import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip
from PyQt5.uic import loadUi


class Window(QMainWindow):
    GLOBAL_STATE = 0
    def __init__(self):
        super(Window, self).__init__()
        loadUi('./basicUi.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.btn_close.setToolTip("Close")
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.setToolTip("Minimize")
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_maximize.setToolTip("Maximize")
        self.btn_maximize.clicked.connect(self.maximize)
        self.oldPos = self.pos()
        self.show()

    def mousePressEvent(self, event) -> None:
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event) -> None:
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move((delta.x() + self.x()), (self.y() + delta.y()))
        self.oldPos = event.globalPos()

    def maximize(self):
        if self.GLOBAL_STATE == 0:
            self.showMaximized()
            self.GLOBAL_STATE = 1
            self.btn_maximize.setToolTip("Restore")
        else:
            self.showNormal()
            self.GLOBAL_STATE = 0
            self.btn_maximize.setToolTip("Maximize")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
