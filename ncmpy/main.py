import sys

from PySide2.QtWidgets import QApplication

from gui.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
