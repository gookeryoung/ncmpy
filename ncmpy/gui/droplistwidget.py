import typing

from PySide2.QtCore import QFileInfo, QUrl, Qt, Signal
from PySide2.QtGui import QDragEnterEvent, QDropEvent
from PySide2.QtWidgets import QListWidget, QListWidgetItem


class DropListWidget(QListWidget):
    dropEnd = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls: typing.List[QUrl] = event.mimeData().urls()
            for url in urls:
                name = url.toLocalFile()
                info = QFileInfo(name)
                if info.suffix() != 'ncm' or info.isDir():
                    continue
                self.add_file(name)
            self.dropEnd.emit()

    def add_file(self, filename):
        item: typing.List[QListWidgetItem] = self.findItems(filename, Qt.MatchExactly)
        if len(item):
            return
        self.addItem(filename)

    def get_next_file(self):
        return self.takeItem(0).text()

    def get_file_count(self):
        return self.count()
