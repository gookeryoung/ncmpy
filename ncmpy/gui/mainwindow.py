from PySide2.QtCore import QDir, QStringListModel
from PySide2.QtWidgets import QMainWindow, QFileDialog

from gui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.pbOpenOutDir.clicked.connect(self.open_out_directory)

        self.out_dirs = QStringListModel([])

    def open_out_directory(self):
        out_dir = QFileDialog.getExistingDirectory(
            self, '输出目录', QDir.homePath(), QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if len(out_dir):
            self.cbOutDir.setCurrentText(out_dir)
