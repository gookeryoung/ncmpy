from PySide2.QtWidgets import QListWidget


class DropListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
