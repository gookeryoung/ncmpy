import sys

from PySide2.QtWidgets import QApplication
from gui.mainwindow import MainWindow
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="light_cyan_500.xml")

    win = MainWindow()
    win.show()

    app.exec_()
