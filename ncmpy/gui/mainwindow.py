import typing

from PySide2.QtCore import QDir, QFileInfo, QThread
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from gui.ui_mainwindow import Ui_MainWindow
from unlocker.unlocker import Unlocker
from config import DIR_TEST, DIR_TEST_FILE


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pbOpenFolder.setFocus()

        self.unlock_thread: typing.Optional[QThread] = None

        # TODO: TEST CODE
        self.cbOutDir.insertItem(0, str(DIR_TEST))
        self.lwFiles.add_file(str(DIR_TEST_FILE))

        self.pbOpenOutDir.clicked.connect(self.open_out_directory)
        self.pbOpenFolder.clicked.connect(self.open_import_directory)
        self.pbProcess.clicked.connect(self.process_files)

    def open_out_directory(self):
        out_dir = QFileDialog.getExistingDirectory(
            self,
            "选择输出目录",
            QDir.homePath(),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        if len(out_dir):
            self.cbOutDir.insertItem(0, out_dir)
            self.cbOutDir.setCurrentIndex(0)

    def open_import_directory(self):
        import_dir = QFileDialog.getExistingDirectory(
            self,
            "选择 ncm 文件所在目录",
            QDir.homePath(),
            QFileDialog.ShowDirsOnly,
        )

        if not import_dir:
            QMessageBox.warning(self, "警告", "未选择任何目录!")
            return

        import_root = QDir(import_dir)
        files: typing.List[str] = import_root.entryList(QDir.Files)
        for file in files:
            if file.endswith(".ncm"):
                self.lwFiles.add_file(import_root.absoluteFilePath(file))

    def process_files(self):
        out_dir = QFileInfo(self.cbOutDir.currentText())
        if not out_dir.exists() or not out_dir.isDir():
            QMessageBox.warning(self, "警告", "输出目录不正确")
            return

        if not self.lwFiles.count():
            QMessageBox.warning(self, "警告", "没有输入文件")
            self.pbOpenOutDir.setFocus()
            return

        if self.unlock_thread:
            QMessageBox.warning(self, "警告", "正在进行解锁...")
            return

        self.pbOpenFolder.setEnabled(False)
        self.pbOpenOutDir.setEnabled(False)
        self.cbOutDir.setEnabled(False)
        self.lwFiles.setEnabled(False)

        self.unlock_thread = Unlocker(parent=self, list_widget=self.lwFiles, out_dir=out_dir.absoluteFilePath())
        self.unlock_thread.start()
        self.unlock_thread.unlocked.connect(self.unlocked)
        self.unlock_thread.finished.connect(self.all_finished)

    def unlocked(self, current_count: int, total_count: int) -> None:
        self.progressBar.setValue(current_count / total_count)

    def all_finished(self):
        self.disconnect(self.unlock_thread)
        self.unlock_thread.deleteLater()
        self.unlock_thread = None

        QMessageBox.information(self, "提示", "解锁已完成")
        self.progressBar.setValue(0)
        self.cbOutDir.setEnabled(True)
        self.pbOpenFolder.setEnabled(True)
        self.pbOpenOutDir.setEnabled(True)
        self.lwFiles.setEnabled(True)
