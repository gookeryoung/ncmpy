import sys

from PySide2.QtWidgets import QApplication
from qt_material import apply_stylesheet

from gui.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="light_amber.xml")

    win = MainWindow()
    win.show()

    app.exec_()
