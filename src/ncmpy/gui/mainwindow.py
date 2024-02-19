import typing

from PySide2.QtCore import QDir, QFileInfo
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from ncmpy import config
from ncmpy.gui.ui_mainwindow import Ui_MainWindow
from ncmpy.unlocker.unlocker import Unlocker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pbOpenFolder.setFocus()
        self.resize(1440, 900)

        self.cbOutDir.insertItem(0, config.DIR_TEST.as_posix())
        self.lwFiles.add_file(config.DIR_TEST_FILE.as_posix())

        self.pbOpenOutDir.clicked.connect(self.open_out_directory)
        self.pbOpenFolder.clicked.connect(self.open_import_directory)
        self.pbProcess.clicked.connect(self.process_files)

        self.unlocker_thread: typing.Optional[QThread] = None

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

        if not self.lwFiles.get_file_count():
            QMessageBox.warning(self, "警告", "没有输入文件")
            self.pbOpenOutDir.setFocus()
            return

        if self.unlocker_thread:
            QMessageBox.warning(self, "警告", "已启动线程")
            return

        self.pbOpenFolder.setEnabled(False)
        self.pbOpenOutDir.setEnabled(False)
        self.cbOutDir.setEnabled(False)
        self.lwFiles.setEnabled(False)
        self.lwMessage.setEnabled(True)
        self.lwMessage.clear()

        self.unlocker_thread = Unlocker(self.lwFiles, self.cbOutDir.currentText())
        self.unlocker_thread.sig_msg_updated.connect(self.on_msg)
        self.unlocker_thread.finished.connect(self.on_all_finished)
        self.unlocker_thread.sig_unlocked.connect(self.on_unlocked)
        self.unlocker_thread.start()

    def on_unlocked(self, unlocked_count: int, total_count: int) -> None:
        self.progressBar.setValue(unlocked_count / total_count)

    def on_msg(self, msg: str):
        self.lwMessage.addItem(msg)

    def on_all_finished(self):
        self.disconnect(self.unlocker_thread)
        self.unlocker_thread.deleteLater()
        self.unlocker_thread = None

        QMessageBox.information(self, "提示", "解锁已完成")
        self.cbOutDir.setEnabled(True)
        self.pbOpenFolder.setEnabled(True)
        self.pbOpenOutDir.setEnabled(True)
        self.lwFiles.setEnabled(True)
