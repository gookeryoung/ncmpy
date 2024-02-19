from PySide2.QtCore import QRunnable, Signal, QObject

from ncmdump.core import ncmdump as ncmdump


class UnlockRunner(QRunnable, QObject):
    runner_finished = Signal()

    def __init__(self, input_path: str, out_dir: str):
        super().__init__()

        self.input_path = input_path
        self.out_dir = out_dir

    def run(self):
        ncmdump(self.input_path, self.out_dir)
        self.runner_finished.emit()
